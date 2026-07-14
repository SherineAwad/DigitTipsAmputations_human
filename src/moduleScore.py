import scanpy as sc
import pandas as pd
import argparse


def load_genes(module_file):
    genes = (
        pd.read_csv(module_file, header=None)[0]
        .dropna()
        .astype(str)
        .str.strip()
        .tolist()
    )

    return set(genes)


def compute_module_score(adata, genes):

    if "gene_name" not in adata.var.columns:
        raise ValueError("gene_name column not found in adata.var")

    gene_names = adata.var["gene_name"].astype(str).str.strip()
    mask = gene_names.isin(genes)

    if mask.sum() == 0:
        raise ValueError("No module genes found in adata.var['gene_name']")

    print(f"Matched {mask.sum()} module genes")

    valid_genes = adata.var_names[mask.values].tolist()

    if len(valid_genes) == 0:
        raise ValueError("No valid genes after mapping")

    sc.tl.score_genes(
        adata,
        gene_list=valid_genes,
        score_name="module_score",
        use_raw=False,
        layer="log1p"
    )

    return adata


def main():

    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--genes", required=True)
    parser.add_argument("--prefix", required=True)

    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)

    genes = load_genes(args.genes)

    print(list(genes)[:5])

    adata = compute_module_score(adata, genes)

    # Overall UMAP
    sc.pl.umap(
        adata,
        color="module_score",
        vmin=0,
        vmax=1,
        show=False,
        title=f"{args.prefix}_score",
        save=f"_{args.prefix}_umap.png"
    )

    # UMAP per sample
    if 'sample' in adata.obs.columns:
        for sample in adata.obs['sample'].unique():
            adata_subset = adata[adata.obs['sample'] == sample]

            sc.pl.umap(
                adata_subset,
                color="module_score",
                vmin=0,
                vmax=1,
                show=False,
                title=f"{args.prefix}_{sample}",
                save=f"_{args.prefix}_umap_{sample}.png"
            )



if __name__ == "__main__":
    main()
