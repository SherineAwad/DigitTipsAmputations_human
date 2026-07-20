#!/usr/bin/env python3

import argparse
import os

import matplotlib.pyplot as plt
import scanpy as sc

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--prefix", required=True)

args = parser.parse_args()

adata = sc.read_h5ad(args.input)

print(f"Loaded {adata.n_obs} cells and {adata.n_vars} genes")

os.makedirs("figures", exist_ok=True)

sc.tl.paga(
adata,
groups="leiden"
)

sc.pl.paga(
adata,
color="leiden",
edge_width_scale=0.3,
show=False
)

output_file = f"figures/{args.prefix}_paga_clusters.png"

plt.savefig(
output_file,
bbox_inches="tight",
dpi=150
)

plt.close()

print(f"Plot saved to {output_file}")

