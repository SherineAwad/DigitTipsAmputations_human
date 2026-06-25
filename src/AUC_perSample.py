import scanpy as sc
import pyucell as puc
import matplotlib.pyplot as plt
import numpy as np
import argparse
import os

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Path to h5ad file')
parser.add_argument('--prefix', required=True, help='Prefix for output figures')
parser.add_argument('--genes', required=True, help='Path to txt file with one gene per row')
args = parser.parse_args()

# Read data
adata = sc.read_h5ad(args.input)

# Read genes from txt file (one per row)
with open(args.genes, 'r') as f:
    gene_list = [line.strip() for line in f if line.strip()]

# Map gene symbols to var_names using gene_name column
gene_indices = []
for g in gene_list:
    mask = adata.var['gene_name'].astype(str).str.lower() == g.lower()
    if mask.any():
        gene_indices.append(adata.var[mask].index[0])

# Create signatures dict
signatures = {'AUCell_score': gene_indices}

# Run pyUCell scoring using compute_ucell_scores with correct parameters
puc.compute_ucell_scores(adata, signatures, layer='log1p', suffix='')

print(f"AUCell scores computed for {adata.n_obs} cells")

# Create figures directory if needed
os.makedirs('figures', exist_ok=True)

# Plot 1: Histogram of AUCell scores
fig, ax = plt.subplots(figsize=(10, 6))
ax.hist(adata.obs['AUCell_score'], bins=50, color='steelblue', edgecolor='black')
ax.set_xlabel('AUCell Score')
ax.set_ylabel('Number of Cells')
ax.set_title(f'AUCell Score Distribution\n({args.prefix})')
plt.tight_layout()
plt.savefig(f'figures/{args.prefix}_aucell_histogram.png', dpi=150)
plt.close()

# Plot 2: UMAP colored by AUCell score (if UMAP exists)
if 'X_umap' in adata.obsm:
    fig, ax = plt.subplots(figsize=(10, 8))
    scat = ax.scatter(
        adata.obsm['X_umap'][:, 0],
        adata.obsm['X_umap'][:, 1],
        c=adata.obs['AUCell_score'],
        cmap='viridis',
        s=1,
        alpha=0.6,
        vmin=0,
        vmax=1
    )
    ax.set_xlabel('UMAP1')
    ax.set_ylabel('UMAP2')
    ax.set_title(f'AUCell Score on UMAP ({args.prefix})')
    cbar = plt.colorbar(scat, ax=ax)
    cbar.set_label('AUCell Score')
    plt.tight_layout()
    plt.savefig(f'figures/{args.prefix}_aucell_umap.png', dpi=150)
    plt.close()

# Plot 3: UMAP colored by AUCell score per sample (if UMAP and sample column exist)
if 'X_umap' in adata.obsm and 'sample' in adata.obs.columns:
    unique_samples = adata.obs['sample'].unique()
    for sample in unique_samples:
        fig, ax = plt.subplots(figsize=(10, 8))
        # Subset cells for this sample
        mask = adata.obs['sample'] == sample
        scat = ax.scatter(
            adata.obsm['X_umap'][mask, 0],
            adata.obsm['X_umap'][mask, 1],
            c=adata.obs['AUCell_score'][mask],
            cmap='viridis',
            s=1,
            alpha=0.6,
            vmin=0,
            vmax=1
        )
        ax.set_xlabel('UMAP1')
        ax.set_ylabel('UMAP2')
        ax.set_title(f'AUCell Score - {sample} ({args.prefix})')
        cbar = plt.colorbar(scat, ax=ax)
        cbar.set_label('AUCell Score')
        plt.tight_layout()
        plt.savefig(f'figures/{args.prefix}_aucell_umap_{sample}.png', dpi=150)
        plt.close()

print(f"All figures saved to figures/{args.prefix}_aucell_*.png")
