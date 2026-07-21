import scanpy as sc
import matplotlib.pyplot as plt
import pandas as pd
import argparse
import os
import numpy as np
from scipy.spatial.distance import cdist
from matplotlib.colors import hsv_to_rgb
import matplotlib.cm as cm

# Parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('--input', required=True, help='Path to h5ad file')
parser.add_argument('--prefix', required=True, help='Prefix for output figures')
parser.add_argument("--markers", required=True)

args = parser.parse_args()

# Read data
adata = sc.read_h5ad(args.input)

print(f"Loaded {adata.n_obs} cells and {adata.n_vars} genes")

# Create figures directory
os.makedirs('figures', exist_ok=True)

# Check required columns
if 'leiden' not in adata.obs.columns:
    raise ValueError("Leiden clusters not found in adata.obs")

if 'sample' not in adata.obs.columns:
    raise ValueError("Sample/timepoint column not found in adata.obs")

# -------------------------
# Calculate cluster proportions
# -------------------------

counts = pd.crosstab(
    adata.obs['sample'],
    adata.obs['leiden']
)

proportions = counts.div(
    counts.sum(axis=1),
    axis=0
) * 100

# -------------------------
# Reorder samples to: Uninjured, 3d, 6d, 9d
# -------------------------
desired_order = ['Uninjured', '3d', '6d', '9d']
proportions = proportions.reindex(desired_order)

# -------------------------
# Generate maximally separated colours
# -------------------------

def get_distinct_colors(n):
    """
    Return a list of n distinct RGB colours.
    Uses known categorical palettes for up to 60 colours,
    then falls back to greedy HSV selection.
    """
    if n <= 20:
        # Tab20 palette
        return [cm.tab20(i) for i in range(n)]
    elif n <= 40:
        # Combine Tab20 (first 20) and Tab20b (next 20)
        colors = [cm.tab20(i) for i in range(20)]
        colors += [cm.tab20b(i) for i in range(n - 20)]
        return colors
    elif n <= 60:
        # Combine Tab20, Tab20b, Tab20c
        colors = [cm.tab20(i) for i in range(20)]
        colors += [cm.tab20b(i) for i in range(20)]
        colors += [cm.tab20c(i) for i in range(n - 40)]
        return colors
    else:
        # Fallback: greedy selection from a dense HSV grid with more variation
        hues = np.linspace(0, 1, 500, endpoint=False)
        saturations = np.linspace(0.6, 1.0, 6)
        values = np.linspace(0.6, 1.0, 6)

        candidate_colors = np.array([
            hsv_to_rgb([h, s, v])
            for h in hues
            for s in saturations
            for v in values
        ])

        # Remove duplicates and very dark colors (value < 0.5)
        # Already we have v >= 0.6

        # Greedy: pick the first as the one farthest from grey (0.5,0.5,0.5)
        selected = []
        # Pick the color with maximum distance from grey
        dist_from_grey = np.linalg.norm(candidate_colors - np.array([0.5, 0.5, 0.5]), axis=1)
        first_idx = np.argmax(dist_from_grey)
        selected.append(candidate_colors[first_idx])

        # Remove selected from candidates to avoid re-picking
        candidate_mask = np.ones(len(candidate_colors), dtype=bool)
        candidate_mask[first_idx] = False
        remaining = candidate_colors[candidate_mask]

        for _ in range(1, n):
            if len(remaining) == 0:
                break
            distances = cdist(remaining, np.array(selected), metric='euclidean')
            min_dist = distances.min(axis=1)
            next_idx = np.argmax(min_dist)
            selected.append(remaining[next_idx])
            # Remove chosen from remaining
            remaining = np.delete(remaining, next_idx, axis=0)

        return selected

colors = get_distinct_colors(len(proportions.columns))

# -------------------------
# Plot stacked bar plot
# -------------------------

fig, ax = plt.subplots(figsize=(10, 8))

proportions.plot(
    kind='bar',
    stacked=True,
    ax=ax,
    color=colors
)

ax.set_xlabel('Sample / timepoint')
ax.set_ylabel('Percentage of cells')
ax.set_title(f'Leiden Cluster Composition ({args.prefix})')

ax.legend(
    title='Leiden cluster',
    bbox_to_anchor=(1.05, 1),
    loc='upper left'
)

plt.tight_layout()

output_file = f'figures/{args.prefix}_cluster_composition_stacked_bar.png'

plt.savefig(
    output_file,
    bbox_inches='tight',
    dpi=150
)

plt.close()

print(f"Plot saved to {output_file}")

# Read marker genes from file (one per line)
marker_file = args.markers
marker_genes = []
with open(marker_file, 'r') as f:
    for line in f:
        gene = line.strip()
        if gene:                     # skip empty lines
            marker_genes.append(gene)

# Remove duplicates
marker_genes = list(set(marker_genes))

# Check that gene_name column exists
if 'gene_name' not in adata.var.columns:
    raise ValueError("'gene_name' column not found in adata.var; cannot map symbols.")

# Match against gene symbols
valid_genes = []
for gene in marker_genes:
    if gene in adata.var["gene_name"].values:
        valid_genes.append(gene)
    else:
        print(f"WARNING: {gene} not found in dataset - skipping")

# Feature plots
for gene in valid_genes:
    sc.pl.umap(
        adata,
        color=gene,
        gene_symbols="gene_name",   # show gene symbols
        save=f"_{args.prefix}_{gene}.png"
    )
