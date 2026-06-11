import argparse
from pathlib import Path
import scanpy as sc
import pandas as pd
from scipy.io import mmread


def read_splitpipe(matrix_dir, batch, sample):

    # --------------------
    # LOAD DATA
    # --------------------
    X = mmread(matrix_dir / "count_matrix.mtx").tocsr()
    genes = pd.read_csv(matrix_dir / "all_genes.csv")
    cells = pd.read_csv(matrix_dir / "cell_metadata.csv")

    # --------------------
    # ANN DATA OBJECT (MINIMAL, SAFE)
    # --------------------
    adata = sc.AnnData(X)

    # --------------------
    # CELLS
    # --------------------
    adata.obs = cells.copy()
    adata.obs_names = cells["bc_wells"].astype(str).values
    adata.obs["batch"] = batch
    adata.obs["sample"] = sample

    # --------------------
    # GENES (ONLY SAFE PART HERE)
    # --------------------
    adata.var_names = genes["gene_id"].astype(str).values
    adata.var = pd.DataFrame(index=adata.var_names)

    return adata, genes


def load_list(file):
    return [x.strip() for x in open(file) if x.strip()]


def main(replicates_file, samples_file):

    replicates = load_list(replicates_file)
    samples = load_list(samples_file)

    for rep in replicates:

        rep_dir = Path(rep)

        if not rep_dir.exists():
            print(f"[SKIP] {rep} not found")
            continue

        print(f"[PROCESS] {rep}")

        adatas = []
        gene_ref = None

        for sample in samples:

            path = rep_dir / sample / "DGE_filtered"

            if not path.exists():
                print(f"[WARN] missing {rep}/{sample}")
                continue

            adata, genes = read_splitpipe(
                matrix_dir=path,
                batch=rep,
                sample=sample,
            )

            adatas.append(adata)

            # store gene reference once (they are identical across samples)
            if gene_ref is None:
                gene_ref = genes

        if len(adatas) == 0:
            print(f"[SKIP EMPTY] {rep}")
            continue

        # --------------------
        # CONCAT SAMPLES WITHIN WT
        # --------------------
        adata = sc.concat(
            adatas,
            join="outer",
            index_unique=None,
        )

        # --------------------
        # FIX GENE ANNOTATION AFTER CONCAT (CRITICAL)
        # --------------------
        adata.var["gene_id"] = adata.var_names
        adata.var["gene_name"] = gene_ref["gene_name"].astype(str).values

        # --------------------
        # SAVE OUTPUT
        # --------------------
        out_file = f"{rep}.h5ad"
        adata.write(out_file)

        print(f"[DONE] {out_file}")


if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--replicates", required=True)
    parser.add_argument("--samples", required=True)

    args = parser.parse_args()

    main(args.replicates, args.samples)
