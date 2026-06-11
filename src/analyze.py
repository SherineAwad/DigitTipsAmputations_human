import scanpy as sc
import argparse
import os


def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True)
    parser.add_argument('--output', required=True)
    parser.add_argument('--prefix', required=True)
    args = parser.parse_args()

    # -------------------------
    # LOAD
    # -------------------------
    adata = sc.read_h5ad(args.input).copy()

    print(f"[LOAD] {adata.n_obs} cells × {adata.n_vars} genes")

    os.makedirs("figures", exist_ok=True)

    # -------------------------
    # KEEP RAW COUNTS
    # -------------------------
    adata.layers["counts"] = adata.X.copy()

    # -------------------------
    # HVG SELECTION
    # -------------------------
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=2000,
        flavor="seurat_v3"
    )

    print(f"[HVG] {adata.var['highly_variable'].sum()} genes selected")

    # -------------------------
    # PCA ON HVGs ONLY
    # -------------------------
    adata_pca = adata[:, adata.var["highly_variable"]].copy()

    sc.tl.pca(
        adata_pca,
        n_comps=30,
        svd_solver="arpack"
    )

    adata.obsm["X_pca"] = adata_pca.obsm["X_pca"]

    print("[PCA] done")

    # -------------------------
    # NEIGHBORS + UMAP
    # -------------------------
    sc.pp.neighbors(adata, use_rep="X_pca")
    sc.tl.umap(adata)

    print("[UMAP] done")

    # -------------------------
    # GLOBAL UMAP
    # -------------------------
    sc.pl.umap(
        adata,
        color="sample",
        show=False,
        save=f"_{args.prefix}_umap.png"
    )

    # -------------------------
    # PER-SAMPLE UMAP
    # -------------------------
    for s in adata.obs["sample"].unique():

        sc.pl.umap(
            adata[adata.obs["sample"] == s],
            color="sample",
            title=f"Sample: {s}",
            show=False,
            save=f"_{args.prefix}_umap_{s}.png"
        )

    # -------------------------
    # SAVE OBJECT
    # -------------------------
    adata.write(args.output)

    print(f"[SAVED] {args.output}")


if __name__ == "__main__":
    main()
