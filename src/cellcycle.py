import scanpy as sc
import argparse
import matplotlib.pyplot as plt
import os

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Path to h5ad file')
parser.add_argument('--prefix', required=True, help='Prefix for output figures')
parser.add_argument('--genes', required=True, help='Path to txt file with one gene per line (first 43 = S phase, rest = G2/M)')
args = parser.parse_args()

# Read data
adata = sc.read_h5ad(args.input)

# Read genes
with open(args.genes, 'r') as f:
    gene_list = [line.strip() for line in f if line.strip()]

# Split: first 43 = S phase, rest = G2/M
s_genes = gene_list[:43]
g2m_genes = gene_list[43:]

# Map to var_names
s_indices = []
for g in s_genes:
    mask = adata.var['gene_name'].astype(str).str.lower() == g.lower()
    if mask.any():
        s_indices.append(adata.var[mask].index[0])

g2m_indices = []
for g in g2m_genes:
    mask = adata.var['gene_name'].astype(str).str.lower() == g.lower()
    if mask.any():
        g2m_indices.append(adata.var[mask].index[0])

# Compute cell cycle scores using the built-in function
sc.tl.score_genes_cell_cycle(adata, s_genes=s_indices, g2m_genes=g2m_indices, use_raw=False, layer='log1p')

# Create figures directory
os.makedirs('figures', exist_ok=True)

# Plot 1: UMAP - S phase score (all samples)
fig, ax = plt.subplots(figsize=(10, 8))
scat = ax.scatter(adata.obsm['X_umap'][:, 0], adata.obsm['X_umap'][:, 1],
                  c=adata.obs['S_score'], cmap='viridis', s=1, alpha=0.6)
ax.set_xlabel('UMAP1')
ax.set_ylabel('UMAP2')
ax.set_title(f'S Phase Score ({args.prefix})')
cbar = plt.colorbar(scat, ax=ax)
cbar.set_label('S Score')
plt.tight_layout()
plt.savefig(f'figures/{args.prefix}_sphase_umap.png', dpi=150)
plt.close()

# Plot 2: UMAP - G2/M phase score (all samples)
fig, ax = plt.subplots(figsize=(10, 8))
scat = ax.scatter(adata.obsm['X_umap'][:, 0], adata.obsm['X_umap'][:, 1],
                  c=adata.obs['G2M_score'], cmap='viridis', s=1, alpha=0.6)
ax.set_xlabel('UMAP1')
ax.set_ylabel('UMAP2')
ax.set_title(f'G2/M Phase Score ({args.prefix})')
cbar = plt.colorbar(scat, ax=ax)
cbar.set_label('G2/M Score')
plt.tight_layout()
plt.savefig(f'figures/{args.prefix}_g2m_umap.png', dpi=150)
plt.close()

# Plot 3: UMAP per sample - S phase score
if 'sample' in adata.obs.columns:
    unique_samples = adata.obs['sample'].unique()
    for sample in unique_samples:
        fig, ax = plt.subplots(figsize=(10, 8))
        mask = adata.obs['sample'] == sample
        scat = ax.scatter(adata.obsm['X_umap'][mask, 0], adata.obsm['X_umap'][mask, 1],
                          c=adata.obs['S_score'][mask], cmap='viridis', s=1, alpha=0.6)
        ax.set_xlabel('UMAP1')
        ax.set_ylabel('UMAP2')
        ax.set_title(f'S Phase Score - {sample} ({args.prefix})')
        cbar = plt.colorbar(scat, ax=ax)
        cbar.set_label('S Score')
        plt.tight_layout()
        plt.savefig(f'figures/{args.prefix}_sphase_umap_{sample}.png', dpi=150)
        plt.close()

# Plot 4: UMAP per sample - G2/M phase score
if 'sample' in adata.obs.columns:
    for sample in unique_samples:
        fig, ax = plt.subplots(figsize=(10, 8))
        mask = adata.obs['sample'] == sample
        scat = ax.scatter(adata.obsm['X_umap'][mask, 0], adata.obsm['X_umap'][mask, 1],
                          c=adata.obs['G2M_score'][mask], cmap='viridis', s=1, alpha=0.6)
        ax.set_xlabel('UMAP1')
        ax.set_ylabel('UMAP2')
        ax.set_title(f'G2/M Phase Score - {sample} ({args.prefix})')
        cbar = plt.colorbar(scat, ax=ax)
        cbar.set_label('G2/M Score')
        plt.tight_layout()
        plt.savefig(f'figures/{args.prefix}_g2m_umap_{sample}.png', dpi=150)
        plt.close()

print(f"All figures saved to figures/{args.prefix}_*.png")
