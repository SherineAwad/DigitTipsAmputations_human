import argparse
from pathlib import Path
import scanpy as sc
import pandas as pd


def load_list(file):
    return [x.strip() for x in open(file) if x.strip()]


def main(replicates_file, prefix):

    replicates = load_list(replicates_file)

    adatas = []
    gene_ref = None  # will store gene annotation once

    for s in replicates:

        f = Path(f"{s}_doubletRemoved.h5ad")

        if not f.exists():
            print(f"[SKIP] missing {f}")
            continue

        print(f"[LOAD] {f}")

        adata = sc.read_h5ad(f)

        # -------------------------
        # FIX 1: barcode uniqueness
        # -------------------------
        adata.obs_names = [f"{s}_{x}" for x in adata.obs_names]

        adata.obs["dataset"] = s

        # -------------------------
        # FIX 2: capture gene annotation (ONLY ONCE)
        # -------------------------
        if gene_ref is None:
            if "gene_name" in adata.var.columns:
                gene_ref = adata.var[["gene_name"]].copy()
                print("[INFO] gene_name reference captured")
            else:
                gene_ref = None
                print("[WARN] no gene_name found in first dataset")

        adatas.append(adata)

    if len(adatas) == 0:
        raise RuntimeError("No valid h5ad files found")

    # -------------------------
    # CONCAT
    # -------------------------
    print("[CONCAT] merging objects")

    adata = sc.concat(
        adatas,
        join="outer",
        label="dataset",
        index_unique=None
    )

    # -------------------------
    # FIX 3: restore gene_name
    # -------------------------
    if gene_ref is not None:
        adata.var["gene_name"] = gene_ref.reindex(adata.var_names)["gene_name"].values
        print("[DONE] gene_name restored")

    # -------------------------
    # SAVE
    # -------------------------
    out_file = f"{prefix}.h5ad"
    adata.write(out_file)

    print(f"[SAVED] {out_file}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--replicates", required=True)
    parser.add_argument("--prefix", required=True)

    args = parser.parse_args()

    main(args.replicates, args.prefix)
