import scrublet as scr
import scanpy as sc
import numpy as np
from scipy import sparse
import argparse
import os
import matplotlib.pyplot as plt


# -------------------------
# Args (UPDATED ONLY ADD replicates + prefix)
# -------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--replicates', required=True)
parser.add_argument('--prefix', required=True)
parser.add_argument('--threshold', type=float, default=0.3)

args = parser.parse_args()


# -------------------------
# Load replicate list
# -------------------------
with open(args.replicates) as f:
    replicates = [x.strip() for x in f if x.strip()]


os.makedirs("figures", exist_ok=True)


# -------------------------
# LOOP OVER REPLICATES
# -------------------------
for rep in replicates:

    input_file = f"{rep}_QC_filtered.h5ad"
    output_file = f"{rep}_{args.prefix}.h5ad"

    print(f"\n==============================")
    print(f"[LOAD] {input_file}")
    print(f"==============================")

    # -------------------------
    # Load data
    # -------------------------
    adata = sc.read_h5ad(input_file)

    if not adata.obs_names.is_unique:
        adata.obs_names_make_unique()

    print(f"Loaded {adata.n_obs} cells × {adata.n_vars} genes")

    # -------------------------
    # Prepare matrix
    # -------------------------
    X = adata.X
    if sparse.issparse(X):
        X = X.toarray().astype(np.float32)
    else:
        X = np.array(X, dtype=np.float32)

    # -------------------------
    # Run Scrublet
    # -------------------------
    print("Running Scrublet...")

    scrub = scr.Scrublet(X, expected_doublet_rate=0.06)

    doublet_scores, predicted_doublets = scrub.scrub_doublets(
        min_counts=2,
        min_cells=3,
        min_gene_variability_pctl=85,
        n_prin_comps=30
    )

    # -------------------------
    # APPLY THRESHOLD
    # -------------------------
    final_doublets = doublet_scores > args.threshold

    # -------------------------
    # STORE RESULTS
    # -------------------------
    adata.obs["doublet_score"] = doublet_scores
    adata.obs["predicted_doublet"] = final_doublets.astype(bool)

    print(f"Detected doublets: {final_doublets.sum()} / {adata.n_obs}")

    # -------------------------
    # PLOT
    # -------------------------
    fig, ax = plt.subplots(figsize=(8, 6))
    ax.hist(doublet_scores, bins=50, edgecolor='black')
    ax.axvline(args.threshold, color='red', linestyle='--')
    ax.set_title(f"{rep}_{args.prefix} Scrublet scores")
    ax.set_xlabel("Doublet score")
    ax.set_ylabel("Cells")

    fig.savefig(f"figures/{rep}_{args.prefix}_scrublet_scores.png", dpi=300)
    plt.close(fig)

    # -------------------------
    # REMOVE DOUBLETS
    # -------------------------
    adata = adata[~final_doublets].copy()

    print(f"Remaining cells after filtering: {adata.n_obs}")

    # -------------------------
    # SAVE OUTPUT
    # -------------------------
    adata.write(output_file, compression="gzip")

    print(f"SAVED CLEAN DATASET → {output_file}")
