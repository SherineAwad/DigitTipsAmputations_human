#!/usr/bin/env python3

import argparse
import scanpy as sc

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--prefix", required=True)
parser.add_argument("--markers", required=True)
args = parser.parse_args()

# Read marker file
marker_genes = {}

with open(args.markers) as f:
    for line in f:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        celltype, genes = line.split(":")
        marker_genes[celltype] = [g.strip() for g in genes.split(",")]

adata = sc.read_h5ad(args.input)

# Collect all unique genes
all_genes = []
for genes in marker_genes.values():
    all_genes.extend(genes)

all_genes = list(set(all_genes))

# FIX: match against gene symbols (NOT var_names)
valid_genes = []

for gene in all_genes:
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
