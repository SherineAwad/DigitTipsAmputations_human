import scanpy as sc
import argparse
from pathlib import Path
import os
import glob

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', required=True, help='Input clustered h5ad file')
    parser.add_argument('--prefix', required=True, help='Prefix for all output figures')
    args = parser.parse_args()

    adata = sc.read_h5ad(args.input)
    Path('figures').mkdir(exist_ok=True)


    sc.tl.rank_genes_groups(adata, groupby='leiden', method='wilcoxon', use_raw=False, layer='log1p')

    sc.pl.rank_genes_groups_dotplot(
        adata,
        n_genes=3,
        groupby='leiden',
        gene_symbols="gene_name",
        save=f'_{args.prefix}_dotplot.png'
    )

    for f in glob.glob(f'*{args.prefix}_dotplot.png'):
        os.rename(f, f'figures/{f}')

if __name__ == '__main__':
    main()
