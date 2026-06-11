import scanpy as sc
import argparse


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
    # PCA ON HVGs ONLY (CORRECT WAY)
    # -------------------------
    adata_pca = adata[:, adata.var["highly_variable"]].copy()

    sc.tl.pca(
        adata_pca,
        n_comps=30,
        svd_solver="arpack"
    )

    # store back into original object
    adata.obsm["X_pca"] = adata_pca.obsm["X_pca"]

    print("[PCA] done on HVGs")

    # -------------------------
    # NEIGHBORS GRAPH
    # -------------------------
    sc.pp.neighbors(
        adata,
        use_rep="X_pca"
    )

    # -------------------------
    # UMAP
    # -------------------------
    sc.tl.umap(
        adata,
        random_state=42
    )

    print("[UMAP] done")

    # -------------------------
    # PLOTS
    # -------------------------
    sc.pl.umap(
        adata,
        color=["sample"],
        save=f"_{args.prefix}_umap.png",
        show=False
    )

    # -------------------------
    # SAVE OBJECT
    # -------------------------
    adata.write(args.output)

    print(f"[SAVED] {args.output}")


if __name__ == "__main__":
    main()
