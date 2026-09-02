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

###### Dotplot 
![](figures/dotplot__allWT_clustered_markers_dotplot.png?v=2) 

##### Feature plots 

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


### Dot plot of differentially expressed genes per Leiden cluster

We identify genes that are highly expressed in each cluster, which can help characterize and assign putative cell types.

![](figures/dotplot__allWTClusters_dotplot.png?v=1)

### Matrisome plot 

We used human Matrisome gene list from Naba et al 2012 in the link below: 
[Matrisome list Naba et al 2012](https://docs.google.com/spreadsheets/d/12OslOlOhQQtHMOUKAFFgAQXL2zYX-g9q/edit?usp=sharing&ouid=116662519372268813124&rtpof=true&sd=true)

![](figures/umap_matrisome_matrisome_umap.png?v=2)
![](figures/umap_matrisome_matrisome_umap_Uninjured.png?v=1)
![](figures/umap_matrisome_matrisome_umap_3d.png?v=1)
![](figures/umap_matrisome_matrisome_umap_6d.png?v=1)
![](figures/umap_matrisome_matrisome_umap_9d.png?v=1)

#### Matrisome plots per category 

<img src="figures/umap_matrisome_ECM_Glycoproteins_umap.png?v=2" width="33%" /><img src="figures/umap_matrisome_Collagens_umap.png?v=2" width="33%" /><img src="figures/umap_matrisome_Proteoglycans_umap.png?v=2" width="33%" />

<img src="figures/umap_matrisome_ECM-affiliated_Proteins_umap.png?v=2" width="33%" /><img src="figures/umap_matrisome_Secreted_Factors_umap.png?v=2" width="33%" /><img src="figures/umap_matrisome_ECM_Regulators_umap.png?v=2" width="33%" />


#### A Module score plot for Blastema genes 

We plot module score umap using this list of genes: 
`LRRC17` `GREM1` `WNT16` `MMP16` `MMP13` `CTHRC1` `TNC` `PRICKLE1` `AKAP12` `POSTN` `ADAM12` `OLFML1` `ITM2A` `EPHA3` `CCN5`

**Module score calculation:**  
The module score represents the average expression level of the selected gene set relative to a matched control gene set, calculated using `scanpy.tl.score_genes`. Higher scores indicate stronger enrichment of the module-associated expression program.

![](figures/umap_blastema_Module_umap.png?v=1)
![](figures/umap_blastema_Module_umap_Uninjured.png?v=1)
![](figures/umap_blastema_Module_umap_3d.png?v=1)
![](figures/umap_blastema_Module_umap_6d.png?v=1)
![](figures/umap_blastema_Module_umap_9d.png?v=1)


#### UCell score for blastema genes 

We plot UCell score umap using this list of genes: 
`LRRC17` `GREM1` `WNT16` `MMP16` `MMP13` `CTHRC1` `TNC` `PRICKLE1` `AKAP12` `POSTN` `ADAM12` `OLFML1` `ITM2A` `EPHA3` `CCN5`

UCell score is a rank-based enrichment metric that evaluates whether the input gene set is enriched among the highest expressed genes in each cell (based on gene expression ranking rather than absolute expression values). Here, we used blastema genes. This differs from the matrisome score computed above which represents the average expression level of the selected gene set per cell in the log-normalized expression matrix

- High UCell score → many signature genes are highly ranked → strong activity of that program
- Low UCell score → signature genes are scattered low in ranking → weak or absent program activity

![](figures/blastema_Ucell_umap.png?v=1) 
![](figures/blastema_Ucell_umap_Uninjured.png?v=1) 
![](figures/blastema_Ucell_umap_3d.png?v=1)
![](figures/blastema_Ucell_umap_9d.png?v=1)
![](figures/blastema_Ucell_umap_6d.png?v=1)


#### KNN imputed feature plots for blastema genes 

Unlike conventional feature plots, which display only the measured expression in each individual cell and can be affected by dropout and stochastic variation, KNN-smoothed feature plots improve visualization of gene expression patterns by averaging the expression of each cell with that of its transcriptionally similar neighboring cells. This reduces cell-to-cell noise caused by random dropout and measurement variability, highlighting consistent expression patterns shared across local cellular neighborhoods and revealing underlying expression trends that may be obscured at the single-cell level. As a result, subtle but biologically meaningful cell populations and gene expression programs can become more readily identifiable.

> ⚠️ 🚨⚠️  **Warning:** Think of KNN smoothing as a microscope focus knob, not a truth-creating machine.
>
> - It sharpens **weak, noisy signals that are already present**, making underlying expression patterns easier to visualize.
> - It **does not create new biological signal**. If a signal appears only after KNN smoothing and is absent in the original feature plot, it should be interpreted with caution and verified using the unsmoothed data.


<img src="figures/umap_blastema_imputedfeatureplot_ADAM12.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_GREM1.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_OLFML1.png?v=1" width="33%" />

<img src="figures/umap_blastema_imputedfeatureplot_AKAP12.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_ITM2A.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_POSTN.png?v=1" width="33%" />

<img src="figures/umap_blastema_imputedfeatureplot_CCN5.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_LRRC17.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_PRICKLE1.png?v=1" width="33%" />

<img src="figures/umap_blastema_imputedfeatureplot_CTHRC1.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_MMP13.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_TNC.png?v=1" width="33%" />

<img src="figures/umap_blastema_imputedfeatureplot_EPHA3.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_MMP16.png?v=1" width="33%" /><img src="figures/umap_blastema_imputedfeatureplot_WNT16.png?v=1" width="33%" />


#### UMAP
![](figures/umap_KNN_Imputed_sample.png?v=1)

![](figures/umap_KNN_Imputed_leidenON.png?v=1)

![](figures/umap_KNN_Imputed_leiden.png?v=1)

#### Feature plots 

<img src="figures/umap_KNN_Imputed_ZP2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ZIC3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ZIC1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_XKR4.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_XCL1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WT1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WNT7B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WNT7A.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_WNT6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WNT3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WNT3A.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WNT2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_WNT10A.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WIF1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_WFDC2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_VWF.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_VWC2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_VGLL1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_UPK2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_UPK1A.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_UCMA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TRIM58.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TRIM29.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TRIM10.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_TREML1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TP63.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TP53AIP1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TNXB.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_TNMD.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TMEM158.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TMEM140.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TMEM114.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_TMCC2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TM4SF18.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TLX2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TIE1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_THEM5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_THBS4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_THBS2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TFPI.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_TFAP2B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TCIM.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TBX2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_TACSTD2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_STMN2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_STAB2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ST6GALNAC3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SPTA1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SPRR3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SPRR1B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SPINK6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SP8.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SP7.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SP5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SOX7.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SOX2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SOX18.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SOX17.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SOX10.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SOST.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SNORC.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SLPI.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SLITRK2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SLC4A1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SLC35F1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SLC18A3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SLC14A1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SHOX2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SFN.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SERPINE3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SERPINB7.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SERPINB5.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SERPINB2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SERPINA1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SCN7A.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_SCG3.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_SCEL.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_S100A8.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_S100A1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_S100A14.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_RUNDC3A.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_RSPO2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ROBO4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_RNASE1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_RHEX.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_RHCE.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_RHAG.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_RERGL.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_RELN.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_RAB25.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PURPL.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PTPRZ1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PTHLH.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PTGER3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PRTN3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PRSS56.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PROX1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PRND.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PRLHR.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PRG4.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PRAC1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PPBP.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_POMC.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PODXL.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PMEL.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PLVAP.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PLK1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PKP3.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PIK3C2G.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PI16.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PHOX2B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PHOX2A.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PGM5-AS1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PGLYRP1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PF4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PECAM1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PCAT19.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PAX9.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PAX6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_PAPPA2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_PANX3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_P2RY14.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_OSTN.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_OMG.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_OMD.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_NTRK3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_NRN1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_NRIR.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_NPTX2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_NPR3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_NPFFR2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_NOTCH4.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_NEK2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_NECTIN4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MYO3B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MYCT1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_MUC7.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MUC15.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MT1M.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MT1G.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_MT1F.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MT1E.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MSX2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MSX1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_MS4A3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MPZ.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MNDA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MMRN1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_MMP17.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MME.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MIA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MGP.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_MFAP5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MATN3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MATN1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_MAL.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_MALAT1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LYZ.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LY6G6F-LY6G6D.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LTF.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_LTA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC02587.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC02362.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC02180.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_LINC02008.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC01305.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC01198.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC01133.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_LINC00881.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC00682.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC00567.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC00487.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_LINC00316.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LINC00237.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LGI4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_LCN2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_LAMP5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KRT5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KRT4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KRT1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_KRT17.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KRT15.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KRT13.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KRT12.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_KREMEN2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KLRC1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KLRB1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KERA.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_KDR.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KCNK10.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_KANK3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ITGBL1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_ISL2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ISL1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IRX4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_INSC.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_INA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IL7R.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IL7.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IL6.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_IL2RG.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IHH.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IGSF21.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IGLL1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_IGFL2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IGFBP6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IGDCC3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IFITM5.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_IFIT1B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ICAM2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_IBSP.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HS3ST3A1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_HOXD13.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HOXD12.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HOXC5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HOXC13.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_HOXB-AS3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HOXB9.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HOPX.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HLA-DRA.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_HLA-DQA1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HEPACAM.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HEMGN.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HBZ.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_HBM.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HBG1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HBE1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_HBB.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_HAPLN1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GYPB.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GYPA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GRHL3.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_GPR182.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GPR17.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GPIHBP1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GJB6.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_GJB2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GJA5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GJA4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GIMAP7.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_GIMAP5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GFRA3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GDF5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GDF15.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_GAST.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GAP43.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GABRP.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_GABARAP.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_FZD9.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FOXS1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FOXF1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FOXD3.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_FOLR2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FNDC1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FLT1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FGFBP2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_FGF5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FGF19.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FGF14.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FERMT1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_FCN1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FCER1A.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_FAM107A.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_F10.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_ESM1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ESAM.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ERBB3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_EPYC.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_EPB42.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ELF5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ELF3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ELANE.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_EEF1G.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_EDNRB.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ECSCR.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ECM1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_ECEL1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DSC3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DMP1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DLX5.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_DLX2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DLX1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DLK1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DKK4.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_DKK1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DHH.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DEFB1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DDO.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_DDC.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_DBH.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CYP26A1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CYP19A1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CTSE.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CTRB2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CSTA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CRABP1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CR1L.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CPA6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CPA3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_COX7C.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_COMP.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_COL9A1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_COL6A6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_COL3A1.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_COL2A1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_COL20A1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_COL17A1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CNMD.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CLVS2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLIC3.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLEC3A.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLEC2B.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CLEC1B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLDN7.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLDN6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLDN5.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CLDN4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLDN11.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLDN10.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CLC.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CITED1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CILP2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CHST9.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CHGA.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CHAD.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CFAP57.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CETP.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CELF3.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CDH6.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CDH5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CDH19.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CDC20.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CD93.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CD69.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CBLN2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CAVIN2.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_CAPNS2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CA1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_CA12.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_C1QC.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_C1QB.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_C1QA.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_C19orf33.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_BTC.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_BPIFA2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_BCAN.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ATP10B.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ASPN.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_ARHGAP15.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_APLNR.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_APCDD1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ANGPTL5.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_ALAS2.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_AHSP.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ADIRF.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ADH1B.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_ADGRL4.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ADGRF5.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ACTG1.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ACKR4.png?v=1" width="25%" />
<img src="figures/umap_KNN_Imputed_ACAN.png?v=1" width="25%" /><img src="figures/umap_KNN_Imputed_ABCB5.png?v=1" width="25%" />

#### Annotations 

![](figures/umap_KNN_Imputed_celltypeON.png?v=1)
![](figures/umap_KNN_Imputed_celltype.png?v=1)


### scVI model

scVI is a deep generative model that learns a low-dimensional latent representation of single-cell gene expression data. Instead of directly clustering cells based on the original high-dimensional expression matrix or PCA space, scVI learns a representation that captures underlying biological patterns in the data—such as differences in cell states, differentiation, or transcriptional programs—while accounting for the noise and sparsity inherent to single-cell measurements.

Neighbour graphs, UMAP, and clustering can then be constructed using this learned latent representation. This provides an alternative view of cellular relationships and may reveal differences in cell states, clusters, or transitions compared with conventional PCA-based analysis.


<img src="figures/blastema_scvi_umap_sample.png?v=1" width="33%" /><img src="figures/blastema_scvi_umap_leiden_ON.png?v=1" width="33%" /><img src="figures/blastema_scvi_umap_leiden.png?v=1" width="33%" />

#### Now lets see connectivity using PAGA
PAGA (Partition-Based Graph Abstraction) is a statistical tool that tests whether the number of cells sharing highly similar active gene programs between two distinct cell clusters is greater than what would happen by pure random chance, where similarity means having the closest matching gene expression levels in low-dimensional principal component space.

![](figures/blastema_scvi_scVI_paga_clusters.png?v=1) 

#### Let's now replot the UCell and module scores on the scVI-derived UMAP

##### Module score on the scVI derived UMAP 

![](figures/umap_scVI_Module_umap.png?v=1) 

<img src="figures/umap_scVI_Module_umap_Uninjured.png?v=1" width="25%" /><img src="figures/umap_scVI_Module_umap_3d.png?v=1" width="25%" /><img src="figures/umap_scVI_Module_umap_6d.png?v=1" width="25%" /><img src="figures/umap_scVI_Module_umap_9d.png?v=1" width="25%" />

##### UCell score on the scVI derived UMAP 

![](figures/scVI_Ucell_umap.png?v=1) 

<img src="figures/scVI_Ucell_umap_Uninjured.png?v=1" width="25%" /><img src="figures/scVI_Ucell_umap_3d.png?v=1" width="25%" /><img src="figures/scVI_Ucell_umap_6d.png?v=1" width="25%" /><img src="figures/scVI_Ucell_umap_9d.png?v=1" width="25%" />

#### Cluster decomposition on the scVI derived umap 

![](figures/scVI__cluster_composition_stacked_bar.png?v=1) 

#### UMAP

![](figures/umap_scVI_leiden.png?v=1)
![](figures/umap_scVI_leidenON.png?v=1)
![](figures/umap_scVI_sample.png?v=1)

#### Feature plot for mouse marker blastema genes on scVI dervied umap 

<img src="figures/umap_scVI_GFRA3.png?v=1" width="25%" /><img src="figures/umap_scVI_HBG1.png?v=1" width="25%" /><img src="figures/umap_scVI_GJA5.png?v=1" width="25%" /><img src="figures/umap_scVI_KDR.png?v=1" width="25%" />
<img src="figures/umap_scVI_PRLHR.png?v=1" width="25%" /><img src="figures/umap_scVI_CD69.png?v=1" width="25%" /><img src="figures/umap_scVI_VWF.png?v=1" width="25%" /><img src="figures/umap_scVI_PRG4.png?v=1" width="25%" />
<img src="figures/umap_scVI_COL6A6.png?v=1" width="25%" /><img src="figures/umap_scVI_UCMA.png?v=1" width="25%" /><img src="figures/umap_scVI_RHCE.png?v=1" width="25%" /><img src="figures/umap_scVI_MATN1.png?v=1" width="25%" />
<img src="figures/umap_scVI_EPYC.png?v=1" width="25%" /><img src="figures/umap_scVI_PANX3.png?v=1" width="25%" /><img src="figures/umap_scVI_SCN7A.png?v=1" width="25%" /><img src="figures/umap_scVI_ICAM2.png?v=1" width="25%" />
<img src="figures/umap_scVI_BPIFA2.png?v=1" width="25%" /><img src="figures/umap_scVI_MT1G.png?v=1" width="25%" /><img src="figures/umap_scVI_DLX2.png?v=1" width="25%" /><img src="figures/umap_scVI_CPA3.png?v=1" width="25%" />
<img src="figures/umap_scVI_TLX2.png?v=1" width="25%" /><img src="figures/umap_scVI_DEFB1.png?v=1" width="25%" /><img src="figures/umap_scVI_GRHL3.png?v=1" width="25%" /><img src="figures/umap_scVI_SOST.png?v=1" width="25%" />
<img src="figures/umap_scVI_ELF5.png?v=1" width="25%" /><img src="figures/umap_scVI_MYCT1.png?v=1" width="25%" /><img src="figures/umap_scVI_FOXS1.png?v=1" width="25%" /><img src="figures/umap_scVI_COL9A1.png?v=1" width="25%" />
<img src="figures/umap_scVI_FNDC1.png?v=1" width="25%" /><img src="figures/umap_scVI_S100A1.png?v=1" width="25%" /><img src="figures/umap_scVI_COX7C.png?v=1" width="25%" /><img src="figures/umap_scVI_RERGL.png?v=1" width="25%" />
<img src="figures/umap_scVI_CAPNS2.png?v=1" width="25%" /><img src="figures/umap_scVI_DHH.png?v=1" width="25%" /><img src="figures/umap_scVI_DDC.png?v=1" width="25%" /><img src="figures/umap_scVI_KRT1.png?v=1" width="25%" />
<img src="figures/umap_scVI_ROBO4.png?v=1" width="25%" /><img src="figures/umap_scVI_HOXC13.png?v=1" width="25%" /><img src="figures/umap_scVI_WNT10A.png?v=1" width="25%" /><img src="figures/umap_scVI_LINC00682.png?v=1" width="25%" />
<img src="figures/umap_scVI_COL2A1.png?v=1" width="25%" /><img src="figures/umap_scVI_CRABP1.png?v=1" width="25%" /><img src="figures/umap_scVI_GJA4.png?v=1" width="25%" /><img src="figures/umap_scVI_SOX7.png?v=1" width="25%" />
<img src="figures/umap_scVI_LINC00881.png?v=1" width="25%" /><img src="figures/umap_scVI_LINC01133.png?v=1" width="25%" /><img src="figures/umap_scVI_S100A14.png?v=1" width="25%" /><img src="figures/umap_scVI_CFAP57.png?v=1" width="25%" />
<img src="figures/umap_scVI_CLDN10.png?v=1" width="25%" /><img src="figures/umap_scVI_HAPLN1.png?v=1" width="25%" /><img src="figures/umap_scVI_COMP.png?v=1" width="25%" /><img src="figures/umap_scVI_CELF3.png?v=1" width="25%" />
<img src="figures/umap_scVI_HEPACAM.png?v=1" width="25%" /><img src="figures/umap_scVI_LTF.png?v=1" width="25%" /><img src="figures/umap_scVI_MSX1.png?v=1" width="25%" /><img src="figures/umap_scVI_CDH5.png?v=1" width="25%" />
<img src="figures/umap_scVI_IBSP.png?v=1" width="25%" /><img src="figures/umap_scVI_KRT15.png?v=1" width="25%" /><img src="figures/umap_scVI_SOX2.png?v=1" width="25%" /><img src="figures/umap_scVI_IL7.png?v=1" width="25%" />
<img src="figures/umap_scVI_GPIHBP1.png?v=1" width="25%" /><img src="figures/umap_scVI_PIK3C2G.png?v=1" width="25%" /><img src="figures/umap_scVI_ISL2.png?v=1" width="25%" /><img src="figures/umap_scVI_PECAM1.png?v=1" width="25%" />
<img src="figures/umap_scVI_CPA6.png?v=1" width="25%" /><img src="figures/umap_scVI_PTPRZ1.png?v=1" width="25%" /><img src="figures/umap_scVI_AHSP.png?v=1" width="25%" /><img src="figures/umap_scVI_HOXC5.png?v=1" width="25%" />
<img src="figures/umap_scVI_FGFBP2.png?v=1" width="25%" /><img src="figures/umap_scVI_CAVIN2.png?v=1" width="25%" /><img src="figures/umap_scVI_ERBB3.png?v=1" width="25%" /><img src="figures/umap_scVI_TMEM114.png?v=1" width="25%" />
<img src="figures/umap_scVI_EDNRB.png?v=1" width="25%" /><img src="figures/umap_scVI_ACKR4.png?v=1" width="25%" /><img src="figures/umap_scVI_IGFBP6.png?v=1" width="25%" /><img src="figures/umap_scVI_SHOX2.png?v=1" width="25%" />
<img src="figures/umap_scVI_VWC2.png?v=1" width="25%" /><img src="figures/umap_scVI_LINC02362.png?v=1" width="25%" /><img src="figures/umap_scVI_SLPI.png?v=1" width="25%" /><img src="figures/umap_scVI_TCIM.png?v=1" width="25%" />
<img src="figures/umap_scVI_WNT6.png?v=1" width="25%" /><img src="figures/umap_scVI_WIF1.png?v=1" width="25%" /><img src="figures/umap_scVI_CYP26A1.png?v=1" width="25%" /><img src="figures/umap_scVI_EEF1G.png?v=1" width="25%" />
<img src="figures/umap_scVI_PHOX2A.png?v=1" width="25%" /><img src="figures/umap_scVI_DDO.png?v=1" width="25%" /><img src="figures/umap_scVI_SP5.png?v=1" width="25%" /><img src="figures/umap_scVI_PURPL.png?v=1" width="25%" />
<img src="figures/umap_scVI_S100A8.png?v=1" width="25%" /><img src="figures/umap_scVI_GYPB.png?v=1" width="25%" /><img src="figures/umap_scVI_CDC20.png?v=1" width="25%" /><img src="figures/umap_scVI_THBS2.png?v=1" width="25%" />
<img src="figures/umap_scVI_SLC4A1.png?v=1" width="25%" /><img src="figures/umap_scVI_HLA-DRA.png?v=1" width="25%" /><img src="figures/umap_scVI_TREML1.png?v=1" width="25%" /><img src="figures/umap_scVI_CLDN5.png?v=1" width="25%" />
<img src="figures/umap_scVI_ITGBL1.png?v=1" width="25%" /><img src="figures/umap_scVI_ACAN.png?v=1" width="25%" /><img src="figures/umap_scVI_SERPINB2.png?v=1" width="25%" /><img src="figures/umap_scVI_MUC15.png?v=1" width="25%" />
<img src="figures/umap_scVI_GIMAP7.png?v=1" width="25%" /><img src="figures/umap_scVI_STAB2.png?v=1" width="25%" /><img src="figures/umap_scVI_GJB2.png?v=1" width="25%" /><img src="figures/umap_scVI_CDH6.png?v=1" width="25%" />
<img src="figures/umap_scVI_HOXB-AS3.png?v=1" width="25%" /><img src="figures/umap_scVI_BCAN.png?v=1" width="25%" /><img src="figures/umap_scVI_ZP2.png?v=1" width="25%" /><img src="figures/umap_scVI_SERPINA1.png?v=1" width="25%" />
<img src="figures/umap_scVI_KERA.png?v=1" width="25%" /><img src="figures/umap_scVI_PROX1.png?v=1" width="25%" /><img src="figures/umap_scVI_ALAS2.png?v=1" width="25%" /><img src="figures/umap_scVI_VGLL1.png?v=1" width="25%" />
<img src="figures/umap_scVI_LINC00237.png?v=1" width="25%" /><img src="figures/umap_scVI_KRT17.png?v=1" width="25%" /><img src="figures/umap_scVI_KRT5.png?v=1" width="25%" /><img src="figures/umap_scVI_MPZ.png?v=1" width="25%" />
<img src="figures/umap_scVI_FLT1.png?v=1" width="25%" /><img src="figures/umap_scVI_GAP43.png?v=1" width="25%" /><img src="figures/umap_scVI_NPFFR2.png?v=1" width="25%" /><img src="figures/umap_scVI_APLNR.png?v=1" width="25%" />
<img src="figures/umap_scVI_PAPPA2.png?v=1" width="25%" /><img src="figures/umap_scVI_CSTA.png?v=1" width="25%" /><img src="figures/umap_scVI_GDF15.png?v=1" width="25%" /><img src="figures/umap_scVI_C19orf33.png?v=1" width="25%" />
<img src="figures/umap_scVI_SP8.png?v=1" width="25%" /><img src="figures/umap_scVI_PTGER3.png?v=1" width="25%" /><img src="figures/umap_scVI_SPRR3.png?v=1" width="25%" /><img src="figures/umap_scVI_ADIRF.png?v=1" width="25%" />
<img src="figures/umap_scVI_CHAD.png?v=1" width="25%" /><img src="figures/umap_scVI_MT1F.png?v=1" width="25%" /><img src="figures/umap_scVI_CITED1.png?v=1" width="25%" /><img src="figures/umap_scVI_PF4.png?v=1" width="25%" />
<img src="figures/umap_scVI_LINC01305.png?v=1" width="25%" /><img src="figures/umap_scVI_WNT3A.png?v=1" width="25%" /><img src="figures/umap_scVI_PODXL.png?v=1" width="25%" /><img src="figures/umap_scVI_ASPN.png?v=1" width="25%" />
<img src="figures/umap_scVI_HOXD12.png?v=1" width="25%" /><img src="figures/umap_scVI_HLA-DQA1.png?v=1" width="25%" /><img src="figures/umap_scVI_PKP3.png?v=1" width="25%" /><img src="figures/umap_scVI_MME.png?v=1" width="25%" />
<img src="figures/umap_scVI_LINC00567.png?v=1" width="25%" /><img src="figures/umap_scVI_LINC02180.png?v=1" width="25%" /><img src="figures/umap_scVI_P2RY14.png?v=1" width="25%" /><img src="figures/umap_scVI_TRIM29.png?v=1" width="25%" />
<img src="figures/umap_scVI_LINC02587.png?v=1" width="25%" /><img src="figures/umap_scVI_KRT13.png?v=1" width="25%" /><img src="figures/umap_scVI_SLC14A1.png?v=1" width="25%" /><img src="figures/umap_scVI_LYZ.png?v=1" width="25%" />
<img src="figures/umap_scVI_IGSF21.png?v=1" width="25%" /><img src="figures/umap_scVI_ECEL1.png?v=1" width="25%" /><img src="figures/umap_scVI_DLK1.png?v=1" width="25%" /><img src="figures/umap_scVI_HOXB9.png?v=1" width="25%" />
<img src="figures/umap_scVI_INSC.png?v=1" width="25%" /><img src="figures/umap_scVI_WNT7B.png?v=1" width="25%" /><img src="figures/umap_scVI_OMD.png?v=1" width="25%" /><img src="figures/umap_scVI_RELN.png?v=1" width="25%" />
<img src="figures/umap_scVI_GYPA.png?v=1" width="25%" /><img src="figures/umap_scVI_FGF5.png?v=1" width="25%" /><img src="figures/umap_scVI_TRIM10.png?v=1" width="25%" /><img src="figures/umap_scVI_IFITM5.png?v=1" width="25%" />
<img src="figures/umap_scVI_UPK1A.png?v=1" width="25%" /><img src="figures/umap_scVI_PAX6.png?v=1" width="25%" /><img src="figures/umap_scVI_NECTIN4.png?v=1" width="25%" /><img src="figures/umap_scVI_WNT2.png?v=1" width="25%" />
<img src="figures/umap_scVI_SERPINB5.png?v=1" width="25%" /><img src="figures/umap_scVI_PI16.png?v=1" width="25%" /><img src="figures/umap_scVI_CDH19.png?v=1" width="25%" /><img src="figures/umap_scVI_PRSS56.png?v=1" width="25%" />
<img src="figures/umap_scVI_PMEL.png?v=1" width="25%" /><img src="figures/umap_scVI_HOPX.png?v=1" width="25%" /><img src="figures/umap_scVI_F10.png?v=1" width="25%" /><img src="figures/umap_scVI_GPR17.png?v=1" width="25%" />
<img src="figures/umap_scVI_LGI4.png?v=1" width="25%" /><img src="figures/umap_scVI_CLDN11.png?v=1" width="25%" /><img src="figures/umap_scVI_ABCB5.png?v=1" width="25%" /><img src="figures/umap_scVI_TMEM158.png?v=1" width="25%" />
<img src="figures/umap_scVI_MMRN1.png?v=1" width="25%" /><img src="figures/umap_scVI_IGDCC3.png?v=1" width="25%" /><img src="figures/umap_scVI_DSC3.png?v=1" width="25%" /><img src="figures/umap_scVI_C1QB.png?v=1" width="25%" />
<img src="figures/umap_scVI_SP7.png?v=1" width="25%" /><img src="figures/umap_scVI_DKK4.png?v=1" width="25%" /><img src="figures/umap_scVI_MMP17.png?v=1" width="25%" /><img src="figures/umap_scVI_GDF5.png?v=1" width="25%" />
<img src="figures/umap_scVI_DLX5.png?v=1" width="25%" /><img src="figures/umap_scVI_ARHGAP15.png?v=1" width="25%" /><img src="figures/umap_scVI_SCEL.png?v=1" width="25%" /><img src="figures/umap_scVI_KRT12.png?v=1" width="25%" />
<img src="figures/umap_scVI_CLDN7.png?v=1" width="25%" /><img src="figures/umap_scVI_CR1L.png?v=1" width="25%" /><img src="figures/umap_scVI_HS3ST3A1.png?v=1" width="25%" /><img src="figures/umap_scVI_WT1.png?v=1" width="25%" />
<img src="figures/umap_scVI_XCL1.png?v=1" width="25%" /><img src="figures/umap_scVI_CA1.png?v=1" width="25%" /><img src="figures/umap_scVI_LINC00316.png?v=1" width="25%" /><img src="figures/umap_scVI_ECM1.png?v=1" width="25%" />
<img src="figures/umap_scVI_SERPINE3.png?v=1" width="25%" /><img src="figures/umap_scVI_HBB.png?v=1" width="25%" /><img src="figures/umap_scVI_CA12.png?v=1" width="25%" /><img src="figures/umap_scVI_ZIC3.png?v=1" width="25%" />
<img src="figures/umap_scVI_OSTN.png?v=1" width="25%" /><img src="figures/umap_scVI_CHST9.png?v=1" width="25%" /><img src="figures/umap_scVI_RUNDC3A.png?v=1" width="25%" /><img src="figures/umap_scVI_MT1E.png?v=1" width="25%" />
<img src="figures/umap_scVI_THBS4.png?v=1" width="25%" /><img src="figures/umap_scVI_PCAT19.png?v=1" width="25%" /><img src="figures/umap_scVI_SERPINB7.png?v=1" width="25%" /><img src="figures/umap_scVI_SPRR1B.png?v=1" width="25%" />
<img src="figures/umap_scVI_LCN2.png?v=1" width="25%" /><img src="figures/umap_scVI_PRTN3.png?v=1" width="25%" /><img src="figures/umap_scVI_TP53AIP1.png?v=1" width="25%" /><img src="figures/umap_scVI_RHAG.png?v=1" width="25%" />
<img src="figures/umap_scVI_SFN.png?v=1" width="25%" /><img src="figures/umap_scVI_DLX1.png?v=1" width="25%" /><img src="figures/umap_scVI_TACSTD2.png?v=1" width="25%" /><img src="figures/umap_scVI_LY6G6F-LY6G6D.png?v=1" width="25%" />
<img src="figures/umap_scVI_CLVS2.png?v=1" width="25%" /><img src="figures/umap_scVI_ELANE.png?v=1" width="25%" /><img src="figures/umap_scVI_FAM107A.png?v=1" width="25%" /><img src="figures/umap_scVI_WNT7A.png?v=1" width="25%" />
<img src="figures/umap_scVI_THEM5.png?v=1" width="25%" /><img src="figures/umap_scVI_IGLL1.png?v=1" width="25%" /><img src="figures/umap_scVI_ESM1.png?v=1" width="25%" /><img src="figures/umap_scVI_PLVAP.png?v=1" width="25%" />
<img src="figures/umap_scVI_DKK1.png?v=1" width="25%" /><img src="figures/umap_scVI_FCN1.png?v=1" width="25%" /><img src="figures/umap_scVI_UPK2.png?v=1" width="25%" /><img src="figures/umap_scVI_FZD9.png?v=1" width="25%" />
<img src="figures/umap_scVI_SPINK6.png?v=1" width="25%" /><img src="figures/umap_scVI_TMEM140.png?v=1" width="25%" /><img src="figures/umap_scVI_SNORC.png?v=1" width="25%" /><img src="figures/umap_scVI_GJB6.png?v=1" width="25%" />
<img src="figures/umap_scVI_CLEC2B.png?v=1" width="25%" /><img src="figures/umap_scVI_CHGA.png?v=1" width="25%" /><img src="figures/umap_scVI_DBH.png?v=1" width="25%" /><img src="figures/umap_scVI_MYO3B.png?v=1" width="25%" />
<img src="figures/umap_scVI_CETP.png?v=1" width="25%" /><img src="figures/umap_scVI_SOX18.png?v=1" width="25%" /><img src="figures/umap_scVI_WNT3.png?v=1" width="25%" /><img src="figures/umap_scVI_ADGRF5.png?v=1" width="25%" />
<img src="figures/umap_scVI_TRIM58.png?v=1" width="25%" /><img src="figures/umap_scVI_CLDN4.png?v=1" width="25%" /><img src="figures/umap_scVI_TIE1.png?v=1" width="25%" /><img src="figures/umap_scVI_IHH.png?v=1" width="25%" />
<img src="figures/umap_scVI_CTSE.png?v=1" width="25%" /><img src="figures/umap_scVI_ISL1.png?v=1" width="25%" /><img src="figures/umap_scVI_PGLYRP1.png?v=1" width="25%" /><img src="figures/umap_scVI_XKR4.png?v=1" width="25%" />
<img src="figures/umap_scVI_FOXF1.png?v=1" width="25%" /><img src="figures/umap_scVI_KLRC1.png?v=1" width="25%" /><img src="figures/umap_scVI_CLEC1B.png?v=1" width="25%" /><img src="figures/umap_scVI_ZIC1.png?v=1" width="25%" />
<img src="figures/umap_scVI_KANK3.png?v=1" width="25%" /><img src="figures/umap_scVI_APCDD1.png?v=1" width="25%" /><img src="figures/umap_scVI_FCER1A.png?v=1" width="25%" /><img src="figures/umap_scVI_PGM5-AS1.png?v=1" width="25%" />
<img src="figures/umap_scVI_SPTA1.png?v=1" width="25%" /><img src="figures/umap_scVI_DMP1.png?v=1" width="25%" /><img src="figures/umap_scVI_TMCC2.png?v=1" width="25%" /><img src="figures/umap_scVI_ESAM.png?v=1" width="25%" />
<img src="figures/umap_scVI_C1QC.png?v=1" width="25%" /><img src="figures/umap_scVI_EPB42.png?v=1" width="25%" /><img src="figures/umap_scVI_MNDA.png?v=1" width="25%" /><img src="figures/umap_scVI_IGFL2.png?v=1" width="25%" />
<img src="figures/umap_scVI_LINC00487.png?v=1" width="25%" /><img src="figures/umap_scVI_COL3A1.png?v=1" width="25%" /><img src="figures/umap_scVI_GPR182.png?v=1" width="25%" /><img src="figures/umap_scVI_LTA.png?v=1" width="25%" />
<img src="figures/umap_scVI_ADH1B.png?v=1" width="25%" /><img src="figures/umap_scVI_IL2RG.png?v=1" width="25%" /><img src="figures/umap_scVI_MATN3.png?v=1" width="25%" /><img src="figures/umap_scVI_PRAC1.png?v=1" width="25%" />
<img src="figures/umap_scVI_CILP2.png?v=1" width="25%" /><img src="figures/umap_scVI_HBM.png?v=1" width="25%" /><img src="figures/umap_scVI_ATP10B.png?v=1" width="25%" /><img src="figures/umap_scVI_TBX2.png?v=1" width="25%" />
<img src="figures/umap_scVI_NTRK3.png?v=1" width="25%" /><img src="figures/umap_scVI_BTC.png?v=1" width="25%" /><img src="figures/umap_scVI_TFPI.png?v=1" width="25%" /><img src="figures/umap_scVI_NPR3.png?v=1" width="25%" />
<img src="figures/umap_scVI_NOTCH4.png?v=1" width="25%" /><img src="figures/umap_scVI_MSX2.png?v=1" width="25%" /><img src="figures/umap_scVI_CTRB2.png?v=1" width="25%" /><img src="figures/umap_scVI_HBZ.png?v=1" width="25%" />
<img src="figures/umap_scVI_SOX17.png?v=1" width="25%" /><img src="figures/umap_scVI_CLDN6.png?v=1" width="25%" /><img src="figures/umap_scVI_MUC7.png?v=1" width="25%" /><img src="figures/umap_scVI_CNMD.png?v=1" width="25%" />
<img src="figures/umap_scVI_NRIR.png?v=1" width="25%" /><img src="figures/umap_scVI_KRT4.png?v=1" width="25%" /><img src="figures/umap_scVI_CYP19A1.png?v=1" width="25%" /><img src="figures/umap_scVI_TNMD.png?v=1" width="25%" />
<img src="figures/umap_scVI_INA.png?v=1" width="25%" /><img src="figures/umap_scVI_COL20A1.png?v=1" width="25%" /><img src="figures/umap_scVI_PHOX2B.png?v=1" width="25%" /><img src="figures/umap_scVI_ECSCR.png?v=1" width="25%" />
<img src="figures/umap_scVI_ANGPTL5.png?v=1" width="25%" /><img src="figures/umap_scVI_ACTG1.png?v=1" width="25%" /><img src="figures/umap_scVI_SLC35F1.png?v=1" width="25%" /><img src="figures/umap_scVI_FOXD3.png?v=1" width="25%" />
<img src="figures/umap_scVI_MIA.png?v=1" width="25%" /><img src="figures/umap_scVI_MFAP5.png?v=1" width="25%" /><img src="figures/umap_scVI_FGF14.png?v=1" width="25%" /><img src="figures/umap_scVI_ST6GALNAC3.png?v=1" width="25%" />
<img src="figures/umap_scVI_CLEC3A.png?v=1" width="25%" /><img src="figures/umap_scVI_PAX9.png?v=1" width="25%" /><img src="figures/umap_scVI_IRX4.png?v=1" width="25%" /><img src="figures/umap_scVI_STMN2.png?v=1" width="25%" />
<img src="figures/umap_scVI_POMC.png?v=1" width="25%" /><img src="figures/umap_scVI_SCG3.png?v=1" width="25%" /><img src="figures/umap_scVI_LAMP5.png?v=1" width="25%" /><img src="figures/umap_scVI_HBE1.png?v=1" width="25%" />
<img src="figures/umap_scVI_RAB25.png?v=1" width="25%" /><img src="figures/umap_scVI_MGP.png?v=1" width="25%" /><img src="figures/umap_scVI_LINC01198.png?v=1" width="25%" /><img src="figures/umap_scVI_HOXD13.png?v=1" width="25%" />
<img src="figures/umap_scVI_NEK2.png?v=1" width="25%" /><img src="figures/umap_scVI_MAL.png?v=1" width="25%" /><img src="figures/umap_scVI_RNASE1.png?v=1" width="25%" /><img src="figures/umap_scVI_FOLR2.png?v=1" width="25%" />
<img src="figures/umap_scVI_KCNK10.png?v=1" width="25%" /><img src="figures/umap_scVI_IL6.png?v=1" width="25%" /><img src="figures/umap_scVI_MALAT1.png?v=1" width="25%" /><img src="figures/umap_scVI_ADGRL4.png?v=1" width="25%" />
<img src="figures/umap_scVI_SLC18A3.png?v=1" width="25%" /><img src="figures/umap_scVI_LINC02008.png?v=1" width="25%" /><img src="figures/umap_scVI_GAST.png?v=1" width="25%" /><img src="figures/umap_scVI_IFIT1B.png?v=1" width="25%" />
<img src="figures/umap_scVI_CBLN2.png?v=1" width="25%" /><img src="figures/umap_scVI_CLC.png?v=1" width="25%" /><img src="figures/umap_scVI_COL17A1.png?v=1" width="25%" /><img src="figures/umap_scVI_GIMAP5.png?v=1" width="25%" />
<img src="figures/umap_scVI_GABARAP.png?v=1" width="25%" /><img src="figures/umap_scVI_OMG.png?v=1" width="25%" /><img src="figures/umap_scVI_PRND.png?v=1" width="25%" /><img src="figures/umap_scVI_TFAP2B.png?v=1" width="25%" />
<img src="figures/umap_scVI_WFDC2.png?v=1" width="25%" /><img src="figures/umap_scVI_PPBP.png?v=1" width="25%" /><img src="figures/umap_scVI_GABRP.png?v=1" width="25%" /><img src="figures/umap_scVI_IL7R.png?v=1" width="25%" />
<img src="figures/umap_scVI_MT1M.png?v=1" width="25%" /><img src="figures/umap_scVI_TM4SF18.png?v=1" width="25%" /><img src="figures/umap_scVI_TP63.png?v=1" width="25%" /><img src="figures/umap_scVI_RHEX.png?v=1" width="25%" />
<img src="figures/umap_scVI_FGF19.png?v=1" width="25%" /><img src="figures/umap_scVI_KLRB1.png?v=1" width="25%" /><img src="figures/umap_scVI_ELF3.png?v=1" width="25%" /><img src="figures/umap_scVI_C1QA.png?v=1" width="25%" />
<img src="figures/umap_scVI_NRN1.png?v=1" width="25%" /><img src="figures/umap_scVI_RSPO2.png?v=1" width="25%" /><img src="figures/umap_scVI_PLK1.png?v=1" width="25%" /><img src="figures/umap_scVI_MS4A3.png?v=1" width="25%" />
<img src="figures/umap_scVI_PTHLH.png?v=1" width="25%" /><img src="figures/umap_scVI_SLITRK2.png?v=1" width="25%" /><img src="figures/umap_scVI_FERMT1.png?v=1" width="25%" /><img src="figures/umap_scVI_CD93.png?v=1" width="25%" />
<img src="figures/umap_scVI_KREMEN2.png?v=1" width="25%" /><img src="figures/umap_scVI_CLIC3.png?v=1" width="25%" /><img src="figures/umap_scVI_TNXB.png?v=1" width="25%" /><img src="figures/umap_scVI_HEMGN.png?v=1" width="25%" />
<img src="figures/umap_scVI_SOX10.png?v=1" width="25%" /><img src="figures/umap_scVI_NPTX2.png?v=1" width="25%" />



### Annotations 



### Random Forest-based cell type similarity

We used a Random Forest classifier to quantify transcriptional similarity between conditions. Specifically, the model was trained to distinguish cells from uninjured, 3d, 6d, and 9d samples, allowing us to assess how closely related these states are based on their gene expression profiles.

![](figures/RF_violin_samples.png?v=1) 




