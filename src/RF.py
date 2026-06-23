#!/usr/bin/env python3
# random_forest_classifier.py
# Random Forest version - NO synthetic data, NO dotplot, NO leiden

import argparse
import scanpy as sc
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix, classification_report
from scipy.sparse import issparse
import os
from sklearn.model_selection import train_test_split

def to_dense(X):
    return X.toarray() if issparse(X) else X

def safe_copy_adata(adata, idx):
    """Safely copy AnnData with sparse matrix handling"""
    try:
        return adata[idx].copy()
    except Exception:
        X = adata.X[idx]
        if issparse(X):
            X = X.copy()
        else:
            X = np.array(X)
        
        obs = adata.obs.iloc[idx].copy()
        var = adata.var.copy()
        
        obsm = {}
        if hasattr(adata, 'obsm'):
            for key, value in adata.obsm.items():
                try:
                    obsm[key] = value[idx]
                except:
                    obsm[key] = value
        
        return sc.AnnData(X=X, obs=obs, var=var, obsm=obsm, uns=adata.uns)

def run_control_model(adata, control, hvg_n, n_estimators, max_control_cells, random_state, min_samples_leaf):
    """Train Random Forest using control as positive and other samples as negative"""
    
    all_samples = adata.obs['sample'].unique().tolist()
    print(f"Found samples: {all_samples}")
    
    if control not in all_samples:
        print(f"WARNING: '{control}' not found. Available: {all_samples}")
        print(f"Using first sample '{all_samples[0]}' as control")
        control = all_samples[0]
    
    print(f"Using '{control}' as control")
    
    # Use log1p layer if available
    if 'log1p' in adata.layers:
        print("Using log1p layer for expression data")
        X_to_use = adata.layers['log1p']
        temp_adata = sc.AnnData(X=X_to_use, obs=adata.obs, var=adata.var)
        adata_for_processing = temp_adata
    else:
        print("WARNING: log1p layer not found, using .X")
        adata_for_processing = adata
    
    # Get Control cells for positive class
    ctrl_idx = np.where(adata.obs["sample"] == control)[0]
    train_ctrl = safe_copy_adata(adata_for_processing, ctrl_idx)
    
    # Get all OTHER cells as negative class
    other_idx = np.where(adata.obs["sample"] != control)[0]
    train_other = safe_copy_adata(adata_for_processing, other_idx) if len(other_idx) > 0 else None
    
    if train_ctrl.n_obs < 10 or train_other is None or train_other.n_obs < 10:
        raise RuntimeError(f"Need both '{control}' and other samples for training.")
    
    print(f"Training: {train_ctrl.n_obs} control cells, {train_other.n_obs} other cells")
    
    # Subsample if too many
    if train_ctrl.n_obs > max_control_cells:
        rng = np.random.default_rng(random_state)
        idx = rng.choice(train_ctrl.n_obs, max_control_cells, replace=False)
        train_ctrl = train_ctrl[idx].copy()
        print(f"Subsampled control to {train_ctrl.n_obs} cells")
    
    if train_other.n_obs > max_control_cells:
        rng = np.random.default_rng(random_state)
        idx = rng.choice(train_other.n_obs, max_control_cells, replace=False)
        train_other = train_other[idx].copy()
        print(f"Subsampled other to {train_other.n_obs} cells")

    # Find common genes using ENSEMBL IDs (var_names)
    ctrl_genes = set(train_ctrl.var_names)
    other_genes = set(train_other.var_names)
    common_genes = list(ctrl_genes.intersection(other_genes))
    print(f"Common genes between control and other: {len(common_genes)}")
    
    # Filter both datasets to only common genes
    train_ctrl = train_ctrl[:, common_genes].copy()
    train_other = train_other[:, common_genes].copy()
    print(f"Control genes after common filtering: {train_ctrl.n_vars}")
    print(f"Other genes after common filtering: {train_other.n_vars}")
    
    # Remove zero-variance genes from control
    Xc = to_dense(train_ctrl.X)
    keep = np.var(Xc, axis=0) > 0
    train_ctrl = train_ctrl[:, keep].copy()
    print(f"Control genes after removing zero variance: {train_ctrl.n_vars}")
    
    # ALSO remove zero-variance genes from other
    Xo = to_dense(train_other.X)
    keep_other = np.var(Xo, axis=0) > 0
    train_other = train_other[:, keep_other].copy()
    print(f"Other genes after removing zero variance: {train_other.n_vars}")
    
    # Find common genes again after zero variance removal
    ctrl_genes = set(train_ctrl.var_names)
    other_genes = set(train_other.var_names)
    common_genes = list(ctrl_genes.intersection(other_genes))
    print(f"Common genes after zero variance removal: {len(common_genes)}")
    
    train_ctrl = train_ctrl[:, common_genes].copy()
    train_other = train_other[:, common_genes].copy()
    print(f"Control genes after final common filtering: {train_ctrl.n_vars}")
    print(f"Other genes after final common filtering: {train_other.n_vars}")
    
    # SELECT GENES - if hvg_n=0 use ALL genes
    if hvg_n > 0:
        hvg_n = min(hvg_n, train_ctrl.n_vars)
        print(f"Selecting top {hvg_n} highly variable genes from control...")
        try:
            sc.pp.highly_variable_genes(
                train_ctrl,
                n_top_genes=hvg_n,
                flavor="seurat",
                subset=True
            )
        except Exception as e:
            print(f"HVG selection failed: {e}")
            print("Using genes with highest variance instead...")
            var_values = np.var(to_dense(train_ctrl.X), axis=0)
            var_idx = np.argsort(var_values)[::-1][:hvg_n]
            var_idx = np.sort(var_idx)
            train_ctrl = train_ctrl[:, var_idx].copy()
    else:
        print("Using ALL genes (hvg_n=0)")
    
    print(f"Final control gene count: {train_ctrl.n_vars}")
    
    # Align other samples with the selected genes from control
    train_other = train_other[:, train_ctrl.var_names].copy()
    print(f"Final other gene count: {train_other.n_vars}")
    
    # Verify gene alignment
    if train_other.n_vars != train_ctrl.n_vars:
        raise RuntimeError(f"Gene mismatch: control has {train_ctrl.n_vars}, other has {train_other.n_vars}")
    
    # Get dense matrices for training
    X_ctrl = np.nan_to_num(to_dense(train_ctrl.X))
    X_other = np.nan_to_num(to_dense(train_other.X))
    
    # Split into train and validation (80/20)
    X_ctrl_train, X_ctrl_val, y_ctrl_train, y_ctrl_val = train_test_split(
        X_ctrl, np.ones(len(X_ctrl)), test_size=0.2, random_state=random_state
    )
    X_other_train, X_other_val, y_other_train, y_other_val = train_test_split(
        X_other, np.zeros(len(X_other)), test_size=0.2, random_state=random_state
    )
    
    # Combine training data
    X_train = np.vstack([X_ctrl_train, X_other_train])
    y_train = np.hstack([y_ctrl_train, y_other_train])
    
    # Combine validation data
    X_val = np.vstack([X_ctrl_val, X_other_val])
    y_val = np.hstack([y_ctrl_val, y_other_val])
    
    print(f"Training set: {X_train.shape[0]} cells, {X_train.shape[1]} genes")
    print(f"Validation set: {X_val.shape[0]} cells")
    print(f"Training class distribution: Control={sum(y_train==1)}, Other={sum(y_train==0)}")
    
    # Train Random Forest classifier - NO scaler, use log1p data directly
    model = RandomForestClassifier(
        n_estimators=n_estimators,
        min_samples_leaf=min_samples_leaf,
        random_state=random_state,
        n_jobs=-1,
        class_weight='balanced'
    )
    
    print("Training Random Forest...")
    model.fit(X_train, y_train)
    print("Training complete!")
    
    # Get scores for ALL cells (for output)
    all_scores = []
    all_cells = []
    
    # Score all samples
    for sample_name in all_samples:
        sample_idx = np.where(adata.obs["sample"] == sample_name)[0]
        if len(sample_idx) == 0:
            continue
        
        sample_adata = safe_copy_adata(adata_for_processing, sample_idx)
        sample_adata = sample_adata[:, train_ctrl.var_names].copy()
        X_sample = np.nan_to_num(to_dense(sample_adata.X))
        
        sample_probs = model.predict_proba(X_sample)[:, 1]
        all_scores.extend(sample_probs)
        all_cells.extend(sample_adata.obs_names.tolist())
    
    # Store raw probabilities (NO rescaling)
    all_scores = np.array(all_scores)
    
    # Create fidelity column with raw probabilities
    adata.obs["fidelity"] = np.nan
    for i, cell_name in enumerate(all_cells):
        if cell_name in adata.obs_names:
            adata.obs.loc[cell_name, "fidelity"] = all_scores[i]
    
    # Confusion matrix on VALIDATION set (not training)
    y_val_pred = model.predict(X_val)
    
    print("\n" + "="*50)
    print("VALIDATION SET EVALUATION (held-out cells):")
    print("="*50)
    print("\nConfusion matrix: Control vs all others")
    print(confusion_matrix(y_val, y_val_pred))
    print("\nClassification Report (VALIDATION):")
    print(classification_report(y_val, y_val_pred))
    
    print("\n" + "="*50)
    print("NOTE: Fidelity scores are RAW probabilities (0-1), not rescaled.")
    print("Threshold 0.5 means 50% probability of being control.")
    print("="*50)
    
    return adata, control

def main():
    # Create figures directory
    os.makedirs("figures", exist_ok=True)
    
    parser = argparse.ArgumentParser(description="Random Forest model to score cell similarity to control")
    
    parser.add_argument("--input", required=True, help="Input h5ad file")
    parser.add_argument("--output", required=True, help="Output h5ad file")
    parser.add_argument("--control", default="Uninjured", help="Control sample name")
    parser.add_argument("--prefix", default="RF", help="Prefix for output files")
    parser.add_argument("--hvg_genes", type=int, default=3000, help="Number of HVGs to use (0 = use all genes)")
    parser.add_argument("--n_estimators", type=int, default=100, help="Number of trees in Random Forest")
    parser.add_argument("--min_samples_leaf", type=int, default=10, help="Minimum samples per leaf")
    parser.add_argument("--max_control_cells", type=int, default=10000, help="Maximum cells per class for training")
    parser.add_argument("--random_state", type=int, default=42, help="Random seed")
    
    args = parser.parse_args()

    prefix = f"{args.prefix}_" if args.prefix else ""

    print("Loading data...")
    adata = sc.read_h5ad(args.input)
    
    print("Running Random Forest...")
    print(f"Parameters:")
    print(f"  control={args.control}")
    print(f"  hvg_genes={args.hvg_genes} {'(ALL GENES)' if args.hvg_genes == 0 else ''}")
    print(f"  n_estimators={args.n_estimators}")
    print(f"  min_samples_leaf={args.min_samples_leaf}")
    print(f"  max_control_cells={args.max_control_cells}")
    print(f"  random_state={args.random_state}")
    
    adata, control = run_control_model(
        adata,
        control=args.control,
        hvg_n=args.hvg_genes,
        n_estimators=args.n_estimators,
        max_control_cells=args.max_control_cells,
        random_state=args.random_state,
        min_samples_leaf=args.min_samples_leaf
    )

    # Violin plot by sample
    print("Creating violin plot by sample...")
    groups = adata.obs['sample'].unique().tolist()
    
    fig, ax = plt.subplots(figsize=(10, 6))
    data = []
    valid_groups = []
    
    for group in groups:
        vals = adata.obs.loc[adata.obs["sample"] == group, "fidelity"].dropna().values
        if len(vals) > 0:
            data.append(vals)
            valid_groups.append(group)
            print(f"  {group}: {len(vals)} cells")
    
    if data:
        vp = ax.violinplot(data, positions=range(len(data)), widths=0.6,
                          showmeans=False, showextrema=False, showmedians=True)
        for body in vp["bodies"]:
            body.set_alpha(0.7)
        
        for i, group in enumerate(valid_groups):
            if group == control:
                vp["bodies"][i].set_facecolor('green')
            else:
                vp["bodies"][i].set_facecolor('gray')
        
        ax.set_xticks(range(len(data)))
        ax.set_xticklabels(valid_groups, rotation=45, ha='right')
        ax.set_ylabel("Control probability (fidelity)")
        ax.set_ylim(-0.05, 1.05)
        ax.set_yticks([0.0, 0.2, 0.4, 0.6, 0.8, 1.0])
        ax.axhline(y=0.5, color='red', linestyle='--', alpha=0.3, linewidth=1)
        ax.set_title(f"Probability of being {control} (Random Forest)")
        
        plt.tight_layout()
        plt.savefig(f"figures/{prefix}violin_samples.png", dpi=300, bbox_inches='tight')
        plt.close()
        print(f"  ✅ Saved: figures/{prefix}violin_samples.png")
    else:
        print("  WARNING: No data for violin plot")
        plt.close()

    print(f"Saving results to {args.output}")
    adata.write(args.output)
    print("Done!")

if __name__ == "__main__":
    main()
