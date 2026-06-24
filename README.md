# Parse scRNAseq: Human Digit tips amputations project

## Data Generation (Split-pipe preprocessing)

Split-pipe output was generated separately for each WT (WT01, WT03, WT04, WT05, WT24, WT36, WT38, WT47), each containing multiple conditions (uninjured, 3d, 6d, 9d) and associated processed outputs.

For each WT, all corresponding samples were imported and combined into a single Scanpy AnnData object, resulting in one h5ad file per WT. Each WT was then treated independently for downstream analysis.

Quality control was performed separately for each WT h5ad object. Pre-filtering and post-filtering QC metrics were generated for each WT to assess data quality and the effect of filtering.

### Pre-filter quality control (WT-level)

Pre-filter QC metrics were visualised for each WT replicate prior to filtering. These plots show distributions of key quality metrics including total counts, number of detected genes, and mitochondrial content.

###### WT01
<img src="figures/violin_WT01_QC_pre_violin.png?v=4" width="90%" />

###### WT03
<img src="figures/violin_WT03_QC_pre_violin.png?v=4" width="90%" />

###### WT04
<img src="figures/violin_WT04_QC_pre_violin.png?v=4" width="90%" />

###### WT05
<img src="figures/violin_WT05_QC_pre_violin.png?v=4" width="90%" />

###### WT24
<img src="figures/violin_WT24_QC_pre_violin.png?v=4" width="90%" />

###### WT36
<img src="figures/violin_WT36_QC_pre_violin.png?v=4" width="90%" />

###### WT38
<img src="figures/violin_WT38_QC_pre_violin.png?v=4" width="90%" />

###### WT47
<img src="figures/violin_WT47_QC_pre_violin.png?v=4" width="90%" />

### Quality control filtering

Cells were filtered using the following quality control thresholds applied consistently across all WT replicates: minimum 500 detected genes per cell, maximum 12,000 genes per cell, minimum 1,000 total counts per cell, maximum 100,000 total counts per cell, and maximum mitochondrial content of 15%.

Genes detected in fewer than 3 cells were removed, and cells with fewer than 200 detected genes were excluded from downstream analysis.

##### Post filtering 

Post-filter QC metrics were visualised for each WT replicate after applying quality control filtering. These plots show the distributions of key quality metrics following removal of low-quality cells.

###### WT01
<img src="figures/violin_WT01_QC_post_violin.png?v=4" width="90%" />

###### WT03
<img src="figures/violin_WT03_QC_post_violin.png?v=4" width="90%" />

###### WT04
<img src="figures/violin_WT04_QC_post_violin.png?v=4" width="90%" />

###### WT05
<img src="figures/violin_WT05_QC_post_violin.png?v=4" width="90%" />

###### WT24
<img src="figures/violin_WT24_QC_post_violin.png?v=4" width="90%" />

###### WT36
<img src="figures/violin_WT36_QC_post_violin.png?v=4" width="90%" />

###### WT38
<img src="figures/violin_WT38_QC_post_violin.png?v=4" width="90%" />

###### WT47
<img src="figures/violin_WT47_QC_post_violin.png?v=4" width="90%" />

##### Before and after filtering stats 

| Sample | Start cells | Final cells | Removed total |
|--------|------------:|------------:|--------------:|
| WT01   | 8875        | 8637        | 238           |
| WT03   | 8697        | 8501        | 196           |
| WT04   | 8769        | 8398        | 371           |
| WT05   | 8727        | 8521        | 206           |
| WT24   | 8815        | 8550        | 265           |
| WT36   | 8596        | 8323        | 273           |
| WT38   | 8043        | 7793        | 250           |
| WT47   | 8196        | 7839        | 357           |


### Doublet detection and removal

Potential doublets (droplets containing more than one cell) were identified for each WT replicate using a computational approach based on transcriptomic similarity patterns. Each cell was assigned a doublet score reflecting the likelihood of being a multiplet.

Cells were classified as doublets using a score threshold of 0.3, and those exceeding this cutoff were removed prior to downstream analysis. The distribution of doublet scores was visualised for each replicate to assess separation between singlets and predicted doublets and to validate the filtering step.

The resulting datasets contain only high-confidence single cells and were used for all subsequent analyses.

#### Doublet score distribution

<img src="figures/WT01_doubletRemoved_scrublet_scores.png?v=4" width="33%" /><img src="figures/WT03_doubletRemoved_scrublet_scores.png?v=4" width="33%" /><img src="figures/WT04_doubletRemoved_scrublet_scores.png?v=4" width="33%" />
<img src="figures/WT05_doubletRemoved_scrublet_scores.png?v=4" width="33%" /><img src="figures/WT24_doubletRemoved_scrublet_scores.png?v=4" width="33%" /><img src="figures/WT36_doubletRemoved_scrublet_scores.png?v=4" width="33%" />
<img src="figures/WT38_doubletRemoved_scrublet_scores.png?v=4" width="33%" /><img src="figures/WT47_doubletRemoved_scrublet_scores.png?v=4" width="33%" />


The table below summarises the number of cells before and after doublet removal for each WT replicate, along with the number of predicted doublets removed.

| WT   | Cells before | Doublets removed | Cells after |
|------|-------------:|-----------------:|------------:|
| WT01 | 8637         | 11               | 8626        |
| WT03 | 8501         | 15               | 8486        |
| WT04 | 8398         | 15               | 8383        |
| WT05 | 8521         | 12               | 8509        |
| WT24 | 8550         | 21               | 8529        |
| WT36 | 8323         | 17               | 8306        |
| WT38 | 7793         | 10               | 7783        |
| WT47 | 7839         | 18               | 7821        |

### Integration and downstream analysis

After doublet removal, all WT datasets were merged into a single unified single-cell dataset to enable comparative analysis across replicates. During merging, cell identities were preserved to retain dataset-of-origin information for each cell.

The combined dataset was then processed for downstream analysis, including normalisation, feature selection, dimensionality reduction, and visualization. This allowed the data to be represented in a low-dimensional space while preserving biologically meaningful variation across cells and samples.

The final integrated dataset was used for all downstream analyses, including clustering and cell state identification.


![](figures/umap_analyzed_umap.png?v=4)

###### And per sample 

<img src="figures/umap_analyzed_Uninjured.png?v=4" width="45%" /><img src="figures/umap_analyzed_3d.png?v=4" width="45%" />
<img src="figures/umap_analyzed_6d.png?v=4" width="45%" /><img src="figures/umap_analyzed_9d.png?v=4" width="45%" />

## Clustering and cluster-level quality assessment

After integration and preprocessing, cells were grouped into transcriptionally distinct clusters using unsupervised clustering based on gene expression similarity. The resulting clusters were visualised in a low-dimensional embedding to assess overall structure and separation between cell populations.

To ensure cluster quality, key quality control metrics (including gene complexity, total RNA counts, and mitochondrial content) were evaluated across clusters. This allowed identification of clusters with distinct quality characteristics and supported downstream interpretation of biological versus low-quality or stressed cell populations.


![](figures/umap_allWT_clustered_leiden.png?v=4)

<img src="figures/violin_allWT_clustered_QC_n_genes_by_counts.png?v=4" width="45%" /><img src="figures/violin_allWT_clustered_QC_total_counts.png?v=4" width="45%" />
<img src="figures/violin_allWT_clustered_QC_pct_counts_mt.png?v=4" width="45%" /><img src="figures/violin_allWT_clustered_QC_pct_counts_ribo.png?v=1" width="45%" />


## Preliminary cell type annotation

We used the following marker genes and corresponding cell types as a guide for annotation:

```python
marker_genes = {
    "Macrophage": ["LYZ", "CD68", "CD14", "CSF1R", "AIF1"],
    "Regenerative_Macrophage": ["APOE", "MRC1", "CD163", "TREM2"],
    "Neutrophil": ["S100A8", "S100A9", "FCGR3B", "MPO", "ELANE"],

    "Keratinocyte": ["KRT5", "KRT14", "KRT1", "KRT10", "EPCAM", "CDH1"],
    "Basal_Keratinocyte": ["KRT5", "KRT14", "TP63", "ITGA6", "COL17A1"],

    "Osteoprogenitor": ["RUNX2", "SP7", "ALPL", "COL1A1"],
    "Osteoblast": ["BGLAP", "IBSP", "SPP1", "ALPL", "DMP1"],
    "Osteoclast": ["CTSK", "ACP5", "CALCR", "NFATC1", "DCSTAMP"],

    "Chondrocyte": ["SOX9", "COL2A1", "ACAN", "COMP", "MATN1"],

    "Pericyte": ["RGS5", "PDGFRB", "CSPG4", "MCAM", "KCNJ8"],
    "Smooth_Muscle": ["ACTA2", "MYH11", "TAGLN", "CNN1", "DES"],

    "Schwann": ["SOX10", "S100B", "MPZ", "PLP1", "MBP"],

    "T_Cell": ["CD3D", "CD3E", "TRAC", "CD4", "CD8A", "IL7R"],
    "B_Cell": ["MS4A1", "CD79A", "CD74", "IGHM", "PAX5"],
    "NK_Cell": ["NKG7", "GNLY", "KLRD1", "PRF1"],
}
```

#### Marker genes dot plot and feature plots 

![](figures/dotplot__allWT_clustered_markers_dotplot.png?v=2) 

<img src="figures/umap_allWT_ADGRL3.png?v=7" width="33%" /><img src="figures/umap_allWT_WNT5A.png?v=7" width="33%" /><img src="figures/umap_allWT_PRICKLE1.png?v=7" width="33%" />

<img src="figures/umap_allWT_TNC.png?v=7" width="33%" /><img src="figures/umap_allWT_SEMA5A.png?v=7" width="33%" /><img src="figures/umap_allWT_MPPED2.png?v=7" width="33%" />

<img src="figures/umap_allWT_IGFBP4.png?v=7" width="33%" /><img src="figures/umap_allWT_CACNA1C.png?v=7" width="33%" /><img src="figures/umap_allWT_COL24A1.png?v=7" width="33%" />

<img src="figures/umap_allWT_SMARCA1.png?v=7" width="33%" /><img src="figures/umap_allWT_SUPT3H.png?v=7" width="33%" /><img src="figures/umap_allWT_CERS6.png?v=7" width="33%" />

<img src="figures/umap_allWT_FARP2.png?v=7" width="33%" /><img src="figures/umap_allWT_SH3RF1.png?v=7" width="33%" /><img src="figures/umap_allWT_SMYD3.png?v=7" width="33%" />

<img src="figures/umap_allWT_DIP2A.png?v=7" width="33%" /><img src="figures/umap_allWT_PLPP3.png?v=7" width="33%" /><img src="figures/umap_allWT_PDGFRB.png?v=7" width="33%" />

<img src="figures/umap_allWT_H2AZ2.png?v=7" width="33%" /><img src="figures/umap_allWT_TTLL5.png?v=7" width="33%" /><img src="figures/umap_allWT_SLC24A3.png?v=7" width="33%" />

<img src="figures/umap_allWT_THBS1.png?v=7" width="33%" /><img src="figures/umap_allWT_MYH10.png?v=7" width="33%" /><img src="figures/umap_allWT_ARMCX4.png?v=7" width="33%" />

<img src="figures/umap_allWT_COL6A3.png?v=7" width="33%" /><img src="figures/umap_allWT_COL12A1.png?v=7" width="33%" /><img src="figures/umap_allWT_TUBB.png?v=7" width="33%" />

<img src="figures/umap_allWT_FBLN1.png?v=7" width="33%" /><img src="figures/umap_allWT_MMP16.png?v=7" width="33%" /><img src="figures/umap_allWT_NFATC1.png?v=7" width="33%" />

<img src="figures/umap_allWT_VCAN.png?v=7" width="33%" /><img src="figures/umap_allWT_AEBP1.png?v=7" width="33%" /><img src="figures/umap_allWT_RUNX2.png?v=7" width="33%" />

<img src="figures/umap_allWT_FBXW4.png?v=7" width="33%" /><img src="figures/umap_allWT_PRRX1.png?v=7" width="33%" /><img src="figures/umap_allWT_MORC4.png?v=7" width="33%" />

<img src="figures/umap_allWT_DDAH1.png?v=7" width="33%" /><img src="figures/umap_allWT_AFF3.png?v=7" width="33%" /><img src="figures/umap_allWT_STMN1.png?v=7" width="33%" />

<img src="figures/umap_allWT_PDGFRA.png?v=7" width="33%" /><img src="figures/umap_allWT_UNC5C.png?v=7" width="33%" /><img src="figures/umap_allWT_FBN2.png?v=7" width="33%" />

<img src="figures/umap_allWT_TMEFF1.png?v=7" width="33%" /><img src="figures/umap_allWT_WWP2.png?v=7" width="33%" /><img src="figures/umap_allWT_BNC2.png?v=7" width="33%" />

<img src="figures/umap_allWT_TBC1D16.png?v=7" width="33%" /><img src="figures/umap_allWT_GPR176.png?v=7" width="33%" /><img src="figures/umap_allWT_BCL9.png?v=7" width="33%" />

<img src="figures/umap_allWT_DZIP1L.png?v=7" width="33%" /><img src="figures/umap_allWT_BCAT1.png?v=7" width="33%" /><img src="figures/umap_allWT_SERPINE2.png?v=7" width="33%" />

<img src="figures/umap_allWT_IGFBP3.png?v=7" width="33%" /><img src="figures/umap_allWT_SCRN1.png?v=7" width="33%" /><img src="figures/umap_allWT_PDIA5.png?v=7" width="33%" />

<img src="figures/umap_allWT_COL1A1.png?v=7" width="33%" /><img src="figures/umap_allWT_ADAM12.png?v=7" width="33%" /><img src="figures/umap_allWT_CPXM2.png?v=7" width="33%" />

<img src="figures/umap_allWT_IGFBP5.png?v=7" width="33%" /><img src="figures/umap_allWT_ELN.png?v=7" width="33%" /><img src="figures/umap_allWT_STK26.png?v=7" width="33%" />

<img src="figures/umap_allWT_MEST.png?v=7" width="33%" /><img src="figures/umap_allWT_TUBB4B.png?v=7" width="33%" /><img src="figures/umap_allWT_LRCH2.png?v=7" width="33%" />

<img src="figures/umap_allWT_CSPG4.png?v=7" width="33%" /><img src="figures/umap_allWT_GPR173.png?v=7" width="33%" /><img src="figures/umap_allWT_CTSK.png?v=7" width="33%" />

<img src="figures/umap_allWT_WIF1.png?v=7" width="33%" /><img src="figures/umap_allWT_SORCS2.png?v=7" width="33%" /><img src="figures/umap_allWT_CSGALNACT1.png?v=7" width="33%" />

<img src="figures/umap_allWT_PTGS2.png?v=7" width="33%" /><img src="figures/umap_allWT_SERPING1.png?v=7" width="33%" /><img src="figures/umap_allWT_CAMK4.png?v=7" width="33%" />

<img src="figures/umap_allWT_H2AZ1.png?v=7" width="33%" /><img src="figures/umap_allWT_AJUBA.png?v=7" width="33%" /><img src="figures/umap_allWT_TUBA1B.png?v=7" width="33%" />

<img src="figures/umap_allWT_ZNF518B.png?v=7" width="33%" /><img src="figures/umap_allWT_FAM118A.png?v=7" width="33%" /><img src="figures/umap_allWT_MASP1.png?v=7" width="33%" />

<img src="figures/umap_allWT_CUL7.png?v=7" width="33%" /><img src="figures/umap_allWT_SMC2.png?v=7" width="33%" /><img src="figures/umap_allWT_GRIA3.png?v=7" width="33%" />

<img src="figures/umap_allWT_PAPPA2.png?v=7" width="33%" /><img src="figures/umap_allWT_PTN.png?v=7" width="33%" /><img src="figures/umap_allWT_FHOD3.png?v=7" width="33%" />

<img src="figures/umap_allWT_DCN.png?v=7" width="33%" /><img src="figures/umap_allWT_CUL9.png?v=7" width="33%" /><img src="figures/umap_allWT_FBLIM1.png?v=7" width="33%" />

<img src="figures/umap_allWT_HMGB2.png?v=7" width="33%" /><img src="figures/umap_allWT_FAT3.png?v=7" width="33%" /><img src="figures/umap_allWT_PHLDB2.png?v=7" width="33%" />

<img src="figures/umap_allWT_IGFBP2.png?v=7" width="33%" /><img src="figures/umap_allWT_AKAP12.png?v=7" width="33%" /><img src="figures/umap_allWT_CXCL14.png?v=7" width="33%" />

<img src="figures/umap_allWT_ERMP1.png?v=7" width="33%" /><img src="figures/umap_allWT_ANK3.png?v=7" width="33%" /><img src="figures/umap_allWT_ADAMTSL3.png?v=7" width="33%" />

<img src="figures/umap_allWT_PAK3.png?v=7" width="33%" /><img src="figures/umap_allWT_GPM6B.png?v=7" width="33%" /><img src="figures/umap_allWT_TCF7.png?v=7" width="33%" />

<img src="figures/umap_allWT_IGDCC4.png?v=7" width="33%" /><img src="figures/umap_allWT_NELL2.png?v=7" width="33%" /><img src="figures/umap_allWT_CRLF1.png?v=7" width="33%" />

<img src="figures/umap_allWT_ACAN.png?v=7" width="33%" /><img src="figures/umap_allWT_ANGPT1.png?v=7" width="33%" /><img src="figures/umap_allWT_POSTN.png?v=7" width="33%" />

<img src="figures/umap_allWT_WDR6.png?v=7" width="33%" /><img src="figures/umap_allWT_RGS3.png?v=7" width="33%" /><img src="figures/umap_allWT_PTX3.png?v=7" width="33%" />

<img src="figures/umap_allWT_PYGB.png?v=7" width="33%" /><img src="figures/umap_allWT_TNFAIP2.png?v=7" width="33%" /><img src="figures/umap_allWT_CENPF.png?v=7" width="33%" />

<img src="figures/umap_allWT_COL2A1.png?v=7" width="33%" /><img src="figures/umap_allWT_BCL7A.png?v=7" width="33%" /><img src="figures/umap_allWT_TMTC4.png?v=7" width="33%" />

<img src="figures/umap_allWT_PRC1.png?v=7" width="33%" /><img src="figures/umap_allWT_TOP2A.png?v=7" width="33%" /><img src="figures/umap_allWT_SERINC2.png?v=7" width="33%" />

<img src="figures/umap_allWT_HEBP2.png?v=7" width="33%" /><img src="figures/umap_allWT_FNDC1.png?v=7" width="33%" /><img src="figures/umap_allWT_ASPN.png?v=7" width="33%" />

<img src="figures/umap_allWT_CKS2.png?v=7" width="33%" /><img src="figures/umap_allWT_CCBE1.png?v=7" width="33%" /><img src="figures/umap_allWT_OBSL1.png?v=7" width="33%" />

<img src="figures/umap_allWT_IFITM1.png?v=7" width="33%" /><img src="figures/umap_allWT_CENPE.png?v=7" width="33%" /><img src="figures/umap_allWT_IMPA2.png?v=7" width="33%" />

<img src="figures/umap_allWT_ADAM19.png?v=7" width="33%" /><img src="figures/umap_allWT_GREM1.png?v=7" width="33%" /><img src="figures/umap_allWT_SCARA5.png?v=7" width="33%" />

<img src="figures/umap_allWT_CAPN6.png?v=7" width="33%" /><img src="figures/umap_allWT_CEBPD.png?v=7" width="33%" /><img src="figures/umap_allWT_MGP.png?v=7" width="33%" />

<img src="figures/umap_allWT_HS3ST3B1.png?v=7" width="33%" /><img src="figures/umap_allWT_OGN.png?v=7" width="33%" /><img src="figures/umap_allWT_SOX9.png?v=7" width="33%" />

<img src="figures/umap_allWT_TADA2A.png?v=7" width="33%" /><img src="figures/umap_allWT_LRRC17.png?v=7" width="33%" /><img src="figures/umap_allWT_COMP.png?v=7" width="33%" />

<img src="figures/umap_allWT_CAD.png?v=7" width="33%" /><img src="figures/umap_allWT_COLQ.png?v=7" width="33%" /><img src="figures/umap_allWT_MKI67.png?v=7" width="33%" />

<img src="figures/umap_allWT_SLITRK6.png?v=7" width="33%" /><img src="figures/umap_allWT_COL25A1.png?v=7" width="33%" /><img src="figures/umap_allWT_S100A4.png?v=7" width="33%" />

<img src="figures/umap_allWT_MOXD1.png?v=7" width="33%" /><img src="figures/umap_allWT_DYNC1I1.png?v=7" width="33%" /><img src="figures/umap_allWT_TAGLN.png?v=7" width="33%" />

<img src="figures/umap_allWT_ALPL.png?v=7" width="33%" /><img src="figures/umap_allWT_GALNT3.png?v=7" width="33%" /><img src="figures/umap_allWT_TIMP1.png?v=7" width="33%" />

<img src="figures/umap_allWT_PANK1.png?v=7" width="33%" /><img src="figures/umap_allWT_L3HYPDH.png?v=7" width="33%" /><img src="figures/umap_allWT_OLFML1.png?v=7" width="33%" />

<img src="figures/umap_allWT_COMMD5.png?v=7" width="33%" /><img src="figures/umap_allWT_BCL11B.png?v=7" width="33%" /><img src="figures/umap_allWT_COL9A1.png?v=7" width="33%" />

<img src="figures/umap_allWT_MATN1.png?v=7" width="33%" /><img src="figures/umap_allWT_NNMT.png?v=7" width="33%" /><img src="figures/umap_allWT_CSF1R.png?v=7" width="33%" />

<img src="figures/umap_allWT_NSG1.png?v=7" width="33%" /><img src="figures/umap_allWT_B4GALT2.png?v=7" width="33%" /><img src="figures/umap_allWT_CCDC8.png?v=7" width="33%" />

<img src="figures/umap_allWT_RBMX2.png?v=7" width="33%" /><img src="figures/umap_allWT_PYCR1.png?v=7" width="33%" /><img src="figures/umap_allWT_EPHA3.png?v=7" width="33%" />

<img src="figures/umap_allWT_MCAM.png?v=7" width="33%" /><img src="figures/umap_allWT_KRT10.png?v=7" width="33%" /><img src="figures/umap_allWT_THBS2.png?v=7" width="33%" />

<img src="figures/umap_allWT_RARRES2.png?v=7" width="33%" /><img src="figures/umap_allWT_PTPRT.png?v=7" width="33%" /><img src="figures/umap_allWT_STC2.png?v=7" width="33%" />

<img src="figures/umap_allWT_CENPA.png?v=7" width="33%" /><img src="figures/umap_allWT_RGS5.png?v=7" width="33%" /><img src="figures/umap_allWT_CPA6.png?v=7" width="33%" />

<img src="figures/umap_allWT_ITGA6.png?v=7" width="33%" /><img src="figures/umap_allWT_SELENOH.png?v=7" width="33%" /><img src="figures/umap_allWT_PAMR1.png?v=7" width="33%" />

<img src="figures/umap_allWT_TPX2.png?v=7" width="33%" /><img src="figures/umap_allWT_LY75.png?v=7" width="33%" /><img src="figures/umap_allWT_MBP.png?v=7" width="33%" />

<img src="figures/umap_allWT_SFRP2.png?v=7" width="33%" /><img src="figures/umap_allWT_ZNF185.png?v=7" width="33%" /><img src="figures/umap_allWT_FAM20A.png?v=7" width="33%" />

<img src="figures/umap_allWT_STRA6.png?v=7" width="33%" /><img src="figures/umap_allWT_DTX4.png?v=7" width="33%" /><img src="figures/umap_allWT_KLRD1.png?v=7" width="33%" />

<img src="figures/umap_allWT_CD68.png?v=7" width="33%" /><img src="figures/umap_allWT_GPX3.png?v=7" width="33%" /><img src="figures/umap_allWT_ANO1.png?v=7" width="33%" />

<img src="figures/umap_allWT_CKS1B.png?v=7" width="33%" /><img src="figures/umap_allWT_C1QTNF3.png?v=7" width="33%" /><img src="figures/umap_allWT_NPR3.png?v=7" width="33%" />

<img src="figures/umap_allWT_ANGPT4.png?v=7" width="33%" /><img src="figures/umap_allWT_SEMA4F.png?v=7" width="33%" /><img src="figures/umap_allWT_MATN3.png?v=7" width="33%" />

<img src="figures/umap_allWT_CCNB2.png?v=7" width="33%" /><img src="figures/umap_allWT_RCOR2.png?v=7" width="33%" /><img src="figures/umap_allWT_SEC16B.png?v=7" width="33%" />

<img src="figures/umap_allWT_COL9A2.png?v=7" width="33%" /><img src="figures/umap_allWT_AMACR.png?v=7" width="33%" /><img src="figures/umap_allWT_CTHRC1.png?v=7" width="33%" />

<img src="figures/umap_allWT_SPC24.png?v=7" width="33%" /><img src="figures/umap_allWT_FAH.png?v=7" width="33%" /><img src="figures/umap_allWT_CCL2.png?v=7" width="33%" />

<img src="figures/umap_allWT_PCLAF.png?v=7" width="33%" /><img src="figures/umap_allWT_GPRC5C.png?v=7" width="33%" /><img src="figures/umap_allWT_CNN1.png?v=7" width="33%" />

<img src="figures/umap_allWT_NUPR1.png?v=7" width="33%" /><img src="figures/umap_allWT_CDK1.png?v=7" width="33%" /><img src="figures/umap_allWT_PLPPR3.png?v=7" width="33%" />

<img src="figures/umap_allWT_OMD.png?v=7" width="33%" /><img src="figures/umap_allWT_PAFAH1B3.png?v=7" width="33%" /><img src="figures/umap_allWT_ADGRG6.png?v=7" width="33%" />

<img src="figures/umap_allWT_GAS2.png?v=7" width="33%" /><img src="figures/umap_allWT_TMEM30B.png?v=7" width="33%" /><img src="figures/umap_allWT_RAB38.png?v=7" width="33%" />

<img src="figures/umap_allWT_ITM2A.png?v=7" width="33%" /><img src="figures/umap_allWT_FIBIN.png?v=7" width="33%" /><img src="figures/umap_allWT_FOXF2.png?v=7" width="33%" />

<img src="figures/umap_allWT_HMMR.png?v=7" width="33%" /><img src="figures/umap_allWT_NOL3.png?v=7" width="33%" /><img src="figures/umap_allWT_H1-5.png?v=7" width="33%" />

<img src="figures/umap_allWT_ADAMTS16.png?v=7" width="33%" /><img src="figures/umap_allWT_BIRC5.png?v=7" width="33%" /><img src="figures/umap_allWT_RBP4.png?v=7" width="33%" />

<img src="figures/umap_allWT_GRB14.png?v=7" width="33%" /><img src="figures/umap_allWT_LRRC75B.png?v=7" width="33%" /><img src="figures/umap_allWT_SP7.png?v=7" width="33%" />

<img src="figures/umap_allWT_UBE2C.png?v=7" width="33%" /><img src="figures/umap_allWT_PLEKHG4.png?v=7" width="33%" /><img src="figures/umap_allWT_CDCA8.png?v=7" width="33%" />

<img src="figures/umap_allWT_MMP13.png?v=7" width="33%" /><img src="figures/umap_allWT_TAC1.png?v=7" width="33%" /><img src="figures/umap_allWT_MYO7A.png?v=7" width="33%" />

<img src="figures/umap_allWT_CCDC167.png?v=7" width="33%" /><img src="figures/umap_allWT_HSPB6.png?v=7" width="33%" /><img src="figures/umap_allWT_RELN.png?v=7" width="33%" />

<img src="figures/umap_allWT_GALE.png?v=7" width="33%" /><img src="figures/umap_allWT_ETV4.png?v=7" width="33%" /><img src="figures/umap_allWT_KCNJ15.png?v=7" width="33%" />

<img src="figures/umap_allWT_PHETA2.png?v=7" width="33%" /><img src="figures/umap_allWT_RAB27B.png?v=7" width="33%" /><img src="figures/umap_allWT_ARSI.png?v=7" width="33%" />

<img src="figures/umap_allWT_MYH11.png?v=7" width="33%" /><img src="figures/umap_allWT_PRKG2.png?v=7" width="33%" /><img src="figures/umap_allWT_ASPHD2.png?v=7" width="33%" />

<img src="figures/umap_allWT_WNT16.png?v=7" width="33%" /><img src="figures/umap_allWT_CHADL.png?v=7" width="33%" /><img src="figures/umap_allWT_JPH2.png?v=7" width="33%" />

<img src="figures/umap_allWT_PAQR6.png?v=7" width="33%" /><img src="figures/umap_allWT_PODNL1.png?v=7" width="33%" /><img src="figures/umap_allWT_PRSS35.png?v=7" width="33%" />

<img src="figures/umap_allWT_CXADR.png?v=7" width="33%" /><img src="figures/umap_allWT_IGF1.png?v=7" width="33%" /><img src="figures/umap_allWT_ENO3.png?v=7" width="33%" />

<img src="figures/umap_allWT_CHI3L1.png?v=7" width="33%" /><img src="figures/umap_allWT_KRT5.png?v=7" width="33%" /><img src="figures/umap_allWT_CXCL2.png?v=7" width="33%" />

<img src="figures/umap_allWT_TP63.png?v=7" width="33%" /><img src="figures/umap_allWT_CDH1.png?v=7" width="33%" /><img src="figures/umap_allWT_CHST1.png?v=7" width="33%" />

<img src="figures/umap_allWT_LCA5L.png?v=7" width="33%" /><img src="figures/umap_allWT_CPNE4.png?v=7" width="33%" /><img src="figures/umap_allWT_CCK.png?v=7" width="33%" />

<img src="figures/umap_allWT_COL17A1.png?v=7" width="33%" /><img src="figures/umap_allWT_DIO2.png?v=7" width="33%" /><img src="figures/umap_allWT_PI15.png?v=7" width="33%" />

<img src="figures/umap_allWT_KRT14.png?v=7" width="33%" /><img src="figures/umap_allWT_GPR27.png?v=7" width="33%" /><img src="figures/umap_allWT_GUCA1A.png?v=7" width="33%" />

<img src="figures/umap_allWT_WNT7B.png?v=7" width="33%" /><img src="figures/umap_allWT_GPER1.png?v=7" width="33%" /><img src="figures/umap_allWT_CTXN1.png?v=7" width="33%" />

<img src="figures/umap_allWT_CPZ.png?v=7" width="33%" /><img src="figures/umap_allWT_EPCAM.png?v=7" width="33%" /><img src="figures/umap_allWT_TNFAIP8L3.png?v=7" width="33%" />

<img src="figures/umap_allWT_SERPINA3.png?v=7" width="33%" /><img src="figures/umap_allWT_BDKRB1.png?v=7" width="33%" /><img src="figures/umap_allWT_CDKN2B.png?v=7" width="33%" />

<img src="figures/umap_allWT_CD4.png?v=7" width="33%" /><img src="figures/umap_allWT_CD74.png?v=7" width="33%" /><img src="figures/umap_allWT_YDJC.png?v=7" width="33%" />

<img src="figures/umap_allWT_MFAP5.png?v=7" width="33%" /><img src="figures/umap_allWT_ITGBL1.png?v=7" width="33%" /><img src="figures/umap_allWT_CD79A.png?v=7" width="33%" />

<img src="figures/umap_allWT_UCN2.png?v=7" width="33%" /><img src="figures/umap_allWT_SOX10.png?v=7" width="33%" /><img src="figures/umap_allWT_BGLAP.png?v=7" width="33%" />

<img src="figures/umap_allWT_KCNJ8.png?v=7" width="33%" /><img src="figures/umap_allWT_IBSP.png?v=7" width="33%" /><img src="figures/umap_allWT_CXCL1.png?v=7" width="33%" />

<img src="figures/umap_allWT_SPP1.png?v=7" width="33%" /><img src="figures/umap_allWT_TNN.png?v=7" width="33%" /><img src="figures/umap_allWT_HOTAIRM1.png?v=7" width="33%" />

<img src="figures/umap_allWT_BMP3.png?v=7" width="33%" /><img src="figures/umap_allWT_MPZ.png?v=7" width="33%" /><img src="figures/umap_allWT_HPGD.png?v=7" width="33%" />

<img src="figures/umap_allWT_CCN5.png?v=7" width="33%" /><img src="figures/umap_allWT_CD14.png?v=7" width="33%" /><img src="figures/umap_allWT_CD8A.png?v=7" width="33%" />

<img src="figures/umap_allWT_CALCR.png?v=7" width="33%" /><img src="figures/umap_allWT_PTGES3L.png?v=7" width="33%" /><img src="figures/umap_allWT_THEM6.png?v=7" width="33%" />

<img src="figures/umap_allWT_STMN2.png?v=7" width="33%" /><img src="figures/umap_allWT_S100B.png?v=7" width="33%" /><img src="figures/umap_allWT_METRN.png?v=7" width="33%" />

<img src="figures/umap_allWT_PLP1.png?v=7" width="33%" /><img src="figures/umap_allWT_APOD.png?v=7" width="33%" /><img src="figures/umap_allWT_TMEM151A.png?v=7" width="33%" />

<img src="figures/umap_allWT_DES.png?v=7" width="33%" /><img src="figures/umap_allWT_KRT1.png?v=7" width="33%" /><img src="figures/umap_allWT_GNLY.png?v=7" width="33%" />

<img src="figures/umap_allWT_CDKN2A.png?v=7" width="33%" /><img src="figures/umap_allWT_IL7R.png?v=7" width="33%" /><img src="figures/umap_allWT_S100A9.png?v=7" width="33%" />

<img src="figures/umap_allWT_GJB3.png?v=7" width="33%" /><img src="figures/umap_allWT_PAX5.png?v=7" width="33%" /><img src="figures/umap_allWT_S100A8.png?v=7" width="33%" />

<img src="figures/umap_allWT_DCSTAMP.png?v=7" width="33%" /><img src="figures/umap_allWT_ELANE.png?v=7" width="33%" /><img src="figures/umap_allWT_AIF1.png?v=7" width="33%" />

<img src="figures/umap_allWT_GJB5.png?v=7" width="33%" /><img src="figures/umap_allWT_PLA1A.png?v=7" width="33%" /><img src="figures/umap_allWT_DMP1.png?v=7" width="33%" />

<img src="figures/umap_allWT_ACP5.png?v=7" width="33%" /><img src="figures/umap_allWT_LYZ.png?v=7" width="33%" /><img src="figures/umap_allWT_TRAC.png?v=7" width="33%" />

<img src="figures/umap_allWT_MPO.png?v=7" width="33%" /><img src="figures/umap_allWT_HP.png?v=7" width="33%" /> <img src="figures/umap_allWT_ZNF354C.png?v=7" width="33%" />

<img src="figures/umap_allWT_SMOC2.png?v=7" width="33%" /><img src="figures/umap_allWT_EFNA4.png?v=7" width="33%" /><img src="figures/umap_allWT_SERP2.png?v=7" width="33%" />

<img src="figures/umap_allWT_FBXO36.png?v=7" width="33%" /><img src="figures/umap_allWT_ACTA2.png?v=7" width="33%" />


### Differentially  expressed genes per cluster ledien 

![](figures/dotplot__allWTClusters_dotplot.png?v=1)

### Matrisome plot 

![](figures/umap_matrisome_matrisome_umap.png?v=1)

#### Matrisome plots per category 

<img src="figures/umap_matrisome_ECM_Glycoproteins_umap.png?v=1" width="33%" /><img src="figures/umap_matrisome_Collagens_umap.png?v=1" width="33%" /><img src="figures/umap_matrisome_Proteoglycans_umap.png?v=1" width="33%" />

<img src="figures/umap_matrisome_ECM-affiliated_Proteins_umap.png?v=1" width="33%" /><img src="figures/umap_matrisome_Secreted_Factors_umap.png?v=1" width="33%" /><img src="figures/umap_matrisome_ECM_Regulators_umap.png?v=1" width="33%" />


#### A score plot using Blastema genes 

![](figures/umap_blastema_matrisome_umap.png?v=1)

### Random Forest celltype simialrity 


![](figures/RF_violin_samples.png?v=1) 




## Preliminary Annotations 


![](figures/umap_allWT_annotated_celltype.png?v=1)
![](figures/umap_allWT_annotated_celltypeON.png?v=1)

