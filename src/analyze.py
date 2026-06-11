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
    # HVG SELECTION (FOR PCA ONLY)
    # -------------------------
    sc.pp.highly_variable_genes(
        adata,
        n_top_genes=2000,
        flavor="seurat_v3"
    )

    print(f"[HVG] {adata.var['highly_variable'].sum()} genes selected")

    # -------------------------
    # PCA ON HVGs ONLY (DO NOT SUBSET OBJECT)
    # -------------------------
    sc.tl.pca(
        adata,
        n_comps=30,
        use_highly_variable=True,
        svd_solver="arpack"
    )

    print("[PCA] done")

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
