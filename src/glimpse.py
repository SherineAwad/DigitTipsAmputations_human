import argparse
import scanpy as sc
import pandas as pd


def glimpse(adata, name="AnnData"):

    print("\n" + "=" * 60)
    print(f"📦 {name} OVERVIEW")
    print("=" * 60)

    print("\n🔢 Shape:")
    print(f"cells x genes = {adata.n_obs} x {adata.n_vars}")

    print("\n🧬 obs (cell metadata):")
    print(adata.obs.head())

    print("\n🧬 obs columns:")
    print(list(adata.obs.columns))

    print("\n🧬 var (gene metadata):")
    print(adata.var.head())

    print("\n🧬 var columns:")
    print(list(adata.var.columns))

    print("\n🏷️ obs keys summary:")
    for col in adata.obs.columns:
        print(f"{col}: {adata.obs[col].nunique()} unique values")

    print("\n🧠 var_names (ENSEMBL) example:")
    print(adata.var_names[:5])

    # ----------------------------------------------------
    # GENE SYMBOL CHECK (IMPORTANT ADDITION)
    # ----------------------------------------------------
    print("\n🧬 gene_name column check:")

    if "gene_name" in adata.var.columns:
        gene_symbols = adata.var["gene_name"].astype(str)

        print("✔ gene_name found in adata.var")
        print("Example gene symbols:")
        print(gene_symbols.head())

        # MT / ribo detection in gene SYMBOL space
        mt_symbols = gene_symbols[gene_symbols.str.upper().str.startswith("MT-")]
        ribo_symbols = gene_symbols[gene_symbols.str.upper().str.startswith(("RPS", "RPL"))]

        print("\n🔋 MT genes (gene_name space):", len(mt_symbols))
        print("Examples:", list(mt_symbols[:10]))

        print("\n🧬 Ribosomal genes (gene_name space):", len(ribo_symbols))
        print("Examples:", list(ribo_symbols[:10]))

    else:
        print("❌ NO gene_name column found in adata.var")

    # ----------------------------------------------------
    # ENSEMBL SPACE CHECK (what you were doing before)
    # ----------------------------------------------------
    print("\n🧪 ENSEMBL-SPACE QC CHECK (var_names only):")

    ensembl = adata.var_names.astype(str)

    mt_ens = ensembl[ensembl.str.upper().str.startswith("MT-")]
    ribo_ens = ensembl[ensembl.str.upper().str.startswith(("RPS", "RPL"))]

    print("MT in ENSEMBL space:", len(mt_ens))
    print("Ribo in ENSEMBL space:", len(ribo_ens))

    print("\n📊 layers:")
    print(list(adata.layers.keys()))

    print("\n📁 uns keys:")
    print(list(adata.uns.keys()))

    print("\n📌 obsm keys:")
    print(list(adata.obsm.keys()))

    print("\n📌 varm keys:")
    print(list(adata.varm.keys()))

    print("\n✔ Done\n")


def main(input_file):

    print(f"[LOADING] {input_file}")
    adata = sc.read_h5ad(input_file)

    glimpse(adata, name=input_file)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)

    args = parser.parse_args()

    main(args.input)
