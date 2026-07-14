import scanpy as sc
import matplotlib.pyplot as plt
import argparse
import os
import numpy as np

# Parse arguments (IDENTICAL to your UCell script)
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

# CHANGE: Match against var["gene_name"]
valid_genes = []
for gene in gene_list:
    if gene in adata.var["gene_name"].values:
        valid_genes.append(gene)
    else:
        print(f"WARNING: {gene} not found in dataset - skipping")

if not valid_genes:
    raise ValueError("No valid genes found in the dataset. Please check your gene list.")

print(f"Found {len(valid_genes)} genes to plot.")

# Ensure UMAP exists
if 'X_umap' not in adata.obsm:
    raise ValueError("No UMAP found in adata.obsm['X_umap']")

# Ensure KNN graph exists (required for smoothing)
if 'neighbors' not in adata.uns:
    print("Computing KNN graph for smoothing...")
    sc.pp.neighbors(adata, n_neighbors=15)

# Extract connectivity matrix and ROW-NORMALIZE it so each row sums to 1
conn = adata.obsp['connectivities'].copy()
row_sums = conn.sum(axis=1).A.flatten()
conn = conn.multiply(1 / row_sums[:, np.newaxis])

# Create figures directory
os.makedirs('figures', exist_ok=True)

# Feature plots - KNN smoothed
for gene in valid_genes:
    print(f"Plotting KNN-smoothed feature plot for: {gene}")
    
    # Get the var_name (Ensembl ID) for this gene symbol
    var_idx = adata.var[adata.var["gene_name"] == gene].index[0]
    
    # Extract log1p normalized expression
    expr = adata[:, var_idx].layers["log1p"]
    if hasattr(expr, 'toarray'):
        expr = expr.toarray()
    expr = np.ravel(expr)
    
    # Manual KNN smoothing using row-normalized connectivity
    smoothed_expr = conn @ expr
    adata.obs[f'{gene}_smoothed'] = smoothed_expr
    
    sc.pl.umap(
        adata,
        color=f'{gene}_smoothed',
        title=f'{gene} (KNN-smoothed)',
        size=10,
        alpha=0.6,
        cmap='viridis',
        save=f"_{args.prefix}_{gene}.png"
    )
    
    # Clean up temporary column
    del adata.obs[f'{gene}_smoothed']

print(f"All KNN-smoothed feature plots saved to figures/umap_{args.prefix}_*.png")
