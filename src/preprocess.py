import argparse
from pathlib import Path
import scanpy as sc


def load_list(file):
    return [x.strip() for x in open(file) if x.strip()]


# ----------------------------
# QC gene setup (FIXED)
# ----------------------------
def ensure_qc_vars(adata):

    if "gene_name" not in adata.var.columns:
        raise ValueError("gene_name column missing in adata.var — required for QC")

    gene_names = adata.var["gene_name"].astype(str)

    adata.var["mt"] = gene_names.str.upper().str.startswith("MT-")
    adata.var["ribo"] = gene_names.str.upper().str.startswith(("RPS", "RPL"))

    sc.pp.calculate_qc_metrics(
        adata,
        qc_vars=["mt", "ribo"],
        inplace=True
    )


# ----------------------------
# QC filtering
# ----------------------------
def filter_cells(adata, args):

    before = adata.n_obs

    sc.pp.filter_cells(adata, min_genes=args.min_genes)
    sc.pp.filter_cells(adata, min_counts=args.min_counts)
    sc.pp.filter_genes(adata, min_cells=args.min_cells_gene)

    after_basic = adata.n_obs

    adata = adata[
        (adata.obs["n_genes_by_counts"] >= args.min_genes_cell) &
        (adata.obs["n_genes_by_counts"] <= args.max_genes) &
        (adata.obs["total_counts"] <= args.max_counts) &
        (adata.obs["pct_counts_mt"] <= args.max_mt)
    ].copy()

    final = adata.n_obs

    print(f"[FILTER STATS]")
    print(f"  Start cells        : {before}")
    print(f"  After basic filter : {after_basic}")
    print(f"  Final cells        : {final}")
    print(f"  Removed total      : {before - final}")

    return adata


# ----------------------------
# Plot helper
# ----------------------------
def plot_violin(adata, sample, prefix, tag):

    sc.pl.violin(
        adata,
        keys=[
            "total_counts",
            "n_genes_by_counts",
            "pct_counts_mt",
            "pct_counts_ribo"
        ],
        groupby="sample",
        multi_panel=True,
        show=False,
        save=f"_{sample}_{prefix}_{tag}_violin.png"
    )


# ----------------------------
# Main pipeline
# ----------------------------
def main(replicates_file, prefix, args):

    samples = load_list(replicates_file)

    figdir = Path("figures")
    sc.settings.figdir = str(figdir)
    figdir.mkdir(exist_ok=True)

    for sample in samples:

        file = Path(f"{sample}.h5ad")

        if not file.exists():
            print(f"[SKIP] missing {file}")
            continue

        print(f"\n[LOAD] {file}")

        adata = sc.read_h5ad(file)
        adata.obs["sample_id"] = sample

        # ------------------------
        # PRE-QC
        # ------------------------
        print(f"[PRE-QC] {sample}")
        ensure_qc_vars(adata)
        plot_violin(adata, sample, prefix, "pre")

        # ------------------------
        # FILTER
        # ------------------------
        print(f"[FILTER] {sample}")
        adata_filt = filter_cells(adata, args)

        # ------------------------
        # POST-QC
        # ------------------------
        print(f"[POST-QC] {sample}")
        ensure_qc_vars(adata_filt)
        plot_violin(adata_filt, sample, prefix, "post")

        # ------------------------
        # SAVE
        # ------------------------
        out_file = Path(f"{sample}_{prefix}_filtered.h5ad")
        adata_filt.write(out_file)

        print(f"[SAVED] {out_file}")


# ----------------------------
# CLI
# ----------------------------
if __name__ == "__main__":

    parser = argparse.ArgumentParser()

    parser.add_argument("--replicates", required=True)
    parser.add_argument("--prefix", required=True)

    parser.add_argument('--min_genes', type=int, default=500)
    parser.add_argument('--max_genes', type=int, default=12000)
    parser.add_argument('--min_counts', type=int, default=1000)
    parser.add_argument('--max_counts', type=int, default=100000)
    parser.add_argument('--max_mt', type=float, default=15)

    parser.add_argument('--min_cells_gene', type=int, default=3)
    parser.add_argument('--min_genes_cell', type=int, default=200)
    args = parser.parse_args()

    main(args.replicates, args.prefix, args)
