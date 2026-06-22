import scanpy as sc
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--output", required=True)
parser.add_argument("--prefix", required=True)
parser.add_argument("--markers", default=None)
args = parser.parse_args()

adata = sc.read(args.input)

# Leiden clustering
sc.tl.leiden(adata, resolution=2.5)

# UMAP (Leiden only)
sc.pl.umap(
    adata,
    color="leiden",
    legend_loc="on data",
    save=f"_{args.prefix}_leiden.png"
)

# QC per Leiden (fix: no figsize inside violin)
qc_metrics = ["n_genes_by_counts", "total_counts", "pct_counts_mt","pct_counts_ribo"]

for qc in qc_metrics:
    if qc in adata.obs:
        sc.pl.violin(
            adata,
            keys=qc,
            groupby="leiden",
            rotation=90,
            stripplot=False,
            jitter=0.2,
            order=sorted(adata.obs["leiden"].unique()),
            show=False,
            save=f"_{args.prefix}_QC_{qc}.png"
        )



if args.markers:

    markers = {}

    with open(args.markers) as f:
        for line in f:
            line = line.strip()
            if not line or ":" not in line:
                continue
            celltype, genes = line.split(":")
            markers[celltype] = [g.strip().replace("\r","") for g in genes.split(",")]

    valid_markers = {}
    for ct, genes in markers.items():
        valid = [g for g in genes if g in adata.var["gene_name"].values]
        if valid:
            valid_markers[ct] = valid

    sc.pl.dotplot(
        adata,
        valid_markers,
        groupby="leiden",
        gene_symbols="gene_name",
        show=False,
        save=f"_{args.prefix}_markers_dotplot.png"
    )

adata.write(args.output, compression="gzip")
