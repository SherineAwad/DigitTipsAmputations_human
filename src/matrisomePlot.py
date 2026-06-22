import argparse
import scanpy as sc
import pandas as pd
import numpy as np


def load_matrisome_genes(matrisome_file):
    # Your file has a metadata row first, real header is row 2
    df = pd.read_csv(matrisome_file, header=1)

    genes = (
        df["Gene Symbol"]
        .dropna()
        .astype(str)
        .str.strip()
        .tolist()
    )

    return set(genes)


def compute_matrisome_score(adata, matrisome_genes):

    if "gene_name" not in adata.var.columns:
        raise ValueError(
            "gene_name column not found in adata.var"
        )

    gene_names = adata.var["gene_name"].astype(str).str.strip()

    mask = gene_names.isin(matrisome_genes)

    if mask.sum() == 0:
        raise ValueError(
            "No matrisome genes found in adata.var['gene_name']"
        )

    X = adata.X[:, mask]

    # sparse-safe mean calculation
    score = np.asarray(X.mean(axis=1)).flatten()

    adata.obs["matrisome_score"] = score

    print(f"Matched {mask.sum()} matrisome genes")

    return adata


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--matrisome_genes", required=True)
    parser.add_argument("--prefix", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)

    matrisome_genes = load_matrisome_genes(
        args.matrisome_genes
    )

    adata = compute_matrisome_score(
        adata,
        matrisome_genes
    )

    sc.pl.umap(
        adata,
        color="matrisome_score",
        show=False,
        save=f"_{args.prefix}_matrisome_umap.png"
    )

    adata.write(args.output)


if __name__ == "__main__":
    main()
