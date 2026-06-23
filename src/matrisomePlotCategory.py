import scanpy as sc
import pandas as pd
import numpy as np
import argparse


def load_matrisome(matrisome_file):
    df = pd.read_csv(matrisome_file, header=1)

    df["Gene Symbol"] = df["Gene Symbol"].astype(str).str.strip()
    df["Matrisome Category"] = df["Matrisome Category"].astype(str).str.strip()

    return df


def compute_category_scores(adata, df):

    if "gene_name" not in adata.var.columns:
        raise ValueError("gene_name column not found in adata.var")

    gene_names = adata.var["gene_name"].astype(str).str.strip()

    # IMPORTANT: use log1p layer only
    adata.X = adata.layers["log1p"]

    categories = df["Matrisome Category"].unique()

    for cat in categories:

        genes = df.loc[df["Matrisome Category"] == cat, "Gene Symbol"].tolist()

        mask = gene_names.isin(genes)

        valid_genes = adata.var_names[mask.values].tolist()

        if len(valid_genes) == 0:
            print(f"Skipping {cat}: no matched genes")
            continue

        sc.tl.score_genes(
            adata,
            gene_list=valid_genes,
            score_name=f"{cat}_score",
            use_raw=False
        )

        print(f"{cat}: {len(valid_genes)} genes used")

    return adata


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--matrisome_genes", required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)

    df = load_matrisome(args.matrisome_genes)

    adata = compute_category_scores(adata, df)

    # plot each category separately
    categories = df["Matrisome Category"].unique()

    for cat in categories:
        score_name = f"{cat}_score"

        if score_name not in adata.obs:
            continue

        sc.pl.umap(
            adata,
            color=score_name,
            show=False,
            save=f"_{args.prefix}_{cat.replace(' ', '_')}_umap.png"
        )

    adata.write(args.output)


if __name__ == "__main__":
    main()
