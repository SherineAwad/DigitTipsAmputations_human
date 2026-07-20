#!/usr/bin/env python3

import scanpy as sc
import scvi
import matplotlib.pyplot as plt
import argparse
import os

# -------------------------
# Parse arguments
# -------------------------
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Path to h5ad file')
parser.add_argument('--output', required=True, help='Output h5ad file')
parser.add_argument('--prefix', required=True, help='Prefix for output files')
parser.add_argument('--latent_dim', type=int, default=30, help='Number of scVI latent dimensions')
parser.add_argument('--epochs', type=int, default=400, help='Number of training epochs')
parser.add_argument('--layer', default='counts', help='Layer containing raw counts')
args = parser.parse_args()

# -------------------------
# Read data
# -------------------------
adata = sc.read_h5ad(args.input)

print(f"Loaded {adata.n_obs} cells and {adata.n_vars} genes")

# -------------------------
# Setup AnnData for scVI
# No batch key because sample/timepoint and celltype
# are biological variables we want to preserve
# -------------------------
scvi.model.SCVI.setup_anndata(
    adata,
    layer=args.layer
)

# -------------------------
# Train SCVI
# -------------------------
model = scvi.model.SCVI(
    adata,
    n_latent=args.latent_dim
)

print("Training scVI model...")
model.train(max_epochs=args.epochs)

# -------------------------
# Extract scVI latent space
# -------------------------
adata.obsm["X_scVI"] = model.get_latent_representation()

print(
    f"scVI latent representation: {adata.obsm['X_scVI'].shape}"
)

# -------------------------
# Compute neighbors and UMAP
# using scVI latent space
# -------------------------
sc.pp.neighbors(
    adata,
    use_rep="X_scVI"
)

sc.tl.umap(adata)

# -------------------------
# Leiden clustering
# -------------------------
sc.tl.leiden(
    adata,
    resolution=1.0
)

# -------------------------
# Create output folders
# -------------------------
os.makedirs("figures", exist_ok=True)
os.makedirs("scvi_model", exist_ok=True)

# -------------------------
# Save trained model
# -------------------------
model.save(
    f"scvi_model/{args.prefix}",
    overwrite=True
)

# -------------------------
# Global UMAP - Leiden clusters
# -------------------------
fig, ax = plt.subplots(figsize=(10, 8))

sc.pl.umap(
    adata,
    color="leiden",
    size=5,
    alpha=0.6,
    show=False,
    ax=ax,
    legend_loc="on data"

)

ax.set_title(
    f"scVI UMAP - Leiden clusters ({args.prefix})"
)

plt.tight_layout()

plt.savefig(
    f"figures/{args.prefix}_umap_leiden_ON.png",
    dpi=150
)

plt.close()

fig, ax = plt.subplots(figsize=(10, 8))

sc.pl.umap(
    adata,
    color="leiden",
    size=5,
    alpha=0.6,
    show=False,
    ax=ax

)

ax.set_title(
    f"scVI UMAP - Leiden clusters ({args.prefix})"
)

plt.tight_layout()

plt.savefig(
    f"figures/{args.prefix}_umap_leiden.png",
    dpi=150
)

plt.close()


# -------------------------
# UMAP colored by sample
# -------------------------
if "sample" in adata.obs.columns:

    fig, ax = plt.subplots(figsize=(10, 8))

    sc.pl.umap(
        adata,
        color="sample",
        size=5,
        alpha=0.6,
        show=False,
        ax=ax
    )

    ax.set_title(
        f"scVI UMAP - Sample ({args.prefix})"
    )

    plt.tight_layout()

    plt.savefig(
        f"figures/{args.prefix}_umap_sample.png",
        dpi=150
    )

    plt.close()


# -------------------------
# UMAP colored by celltype if available
# -------------------------
if "celltype" in adata.obs.columns:

    fig, ax = plt.subplots(figsize=(10, 8))

    sc.pl.umap(
        adata,
        color="celltype",
        size=5,
        alpha=0.6,
        show=False,
        ax=ax
    )

    ax.set_title(
        f"scVI UMAP - Celltype ({args.prefix})"
    )

    plt.tight_layout()

    plt.savefig(
        f"figures/{args.prefix}_umap_celltype.png",
        dpi=150
    )

    plt.close()


# -------------------------
# Save AnnData with scVI embedding
# -------------------------
adata.write_h5ad(args.output)

print("Finished successfully.")
print(f"Saved model: scvi_model/{args.prefix}")
print(f"Saved AnnData: {args.output}")
print("Saved figures in figures/")
