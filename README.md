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

<img src="figures/violin_allWT_clustered_QC_n_genes_by_counts.png?v=4" width="33%" /><img src="figures/violin_allWT_clustered_QC_total_counts.png?v=4" width="33%" /><img src="figures/violin_allWT_clustered_QC_pct_counts_mt.png?v=4" width="33%" />



## Preliminary cell type annotation

We used the following marker genes and corresponding cell types as a guide for annotation:

```python
marker_genes = {
    "Macrophage": ["Lyz", "Cd68", "Cd14", "Csf1r", "Aif1"],
    "Regenerative_Macrophage": ["Apoe", "Mrc1", "Cd163", "Trem2"],
    "Neutrophil": ["S100a8", "S100a9", "Fcgr3b", "Mpo", "Elane"],

    "Keratinocyte": ["Krt5", "Krt14", "Krt1", "Krt10", "Epcam", "Cdh1"],
    "Basal_Keratinocyte": ["Krt5", "Krt14", "Tp63", "Itga6", "Col17a1"],
    "Wound_Epidermis": ["Krt6a", "Krt16", "Fos", "Jun", "Mir21"],

    "Osteoprogenitor": ["Runx2", "Sp7", "Alpl", "Col1a1"],
    "Osteoblast": ["Bglap", "Ibsp", "Spp1", "Alpl", "Dmp1"],
    "Osteoclast": ["Ctsk", "Acp5", "Calcr", "Nfatc1", "Dcstamp"],

    "Chondrocyte": ["Sox9", "Col2a1", "Acan", "Comp", "Matn1"],

    "Pericyte": ["Rgs5", "Pdgfrb", "Cspg4", "Mcam", "Kcnj8"],
    "Smooth_Muscle": ["Acta2", "Myh11", "Tagln", "Cnn1", "Des"],

    "Schwann_Cell": ["Sox10", "S100b", "Mpz", "Plp1", "Mbp"],

    "T_Cell": ["Cd3d", "Cd3e", "Trac", "Cd4", "Cd8a", "Il7r"],
    "B_Cell": ["Ms4a1", "Cd79a", "Cd74", "Ighm", "Pax5"],
    "NK_Cell": ["Nkg7", "Gnly", "Klrd1", "Prf1"],

    "Cycling_Cell": ["Mki67", "Top2a", "Pcna", "Stmn1"],

    "Stress_Response": ["Fos", "Jun", "Hif1a", "Atf3", "Dusp1"]
}
```

#### Marker genes dot plot and feature plots 

<img src="figures/umap_allWT_S100B.png?v=4" width="33%" /><img src="figures/umap_allWT_PAX5.png?v=4" width="33%" /><img src="figures/umap_allWT_MKI67.png?v=4" width="33%" />

<img src="figures/umap_allWT_APOE.png?v=4" width="33%" /><img src="figures/umap_allWT_TRAC.png?v=4" width="33%" /><img src="figures/umap_allWT_PDGFRB.png?v=4" width="33%" />

<img src="figures/umap_allWT_GNLY.png?v=4" width="33%" /><img src="figures/umap_allWT_CDH1.png?v=4" width="33%" /><img src="figures/umap_allWT_RUNX2.png?v=4" width="33%" />

<img src="figures/umap_allWT_DES.png?v=4" width="33%" /><img src="figures/umap_allWT_CSF1R.png?v=4" width="33%" /><img src="figures/umap_allWT_CNN1.png?v=4" width="33%" />

<img src="figures/umap_allWT_MATN1.png?v=4" width="33%" /><img src="figures/umap_allWT_LYZ.png?v=4" width="33%" /><img src="figures/umap_allWT_MPO.png?v=4" width="33%" />

<img src="figures/umap_allWT_KRT10.png?v=4" width="33%" /><img src="figures/umap_allWT_ACP5.png?v=4" width="33%" /><img src="figures/umap_allWT_S100A9.png?v=4" width="33%" />

<img src="figures/umap_allWT_RGS5.png?v=4" width="33%" /><img src="figures/umap_allWT_TOP2A.png?v=4" width="33%" /><img src="figures/umap_allWT_ATF3.png?v=4" width="33%" />

<img src="figures/umap_allWT_IBSP.png?v=4" width="33%" /><img src="figures/umap_allWT_EPCAM.png?v=4" width="33%" /><img src="figures/umap_allWT_SOX10.png?v=4" width="33%" />

<img src="figures/umap_allWT_DMP1.png?v=4" width="33%" /><img src="figures/umap_allWT_PLP1.png?v=4" width="33%" /><img src="figures/umap_allWT_MRC1.png?v=4" width="33%" />

<img src="figures/umap_allWT_BGLAP.png?v=4" width="33%" /><img src="figures/umap_allWT_KRT1.png?v=4" width="33%" /><img src="figures/umap_allWT_CD163.png?v=4" width="33%" />

<img src="figures/umap_allWT_FOS.png?v=4" width="33%" /><img src="figures/umap_allWT_CD8A.png?v=4" width="33%" /><img src="figures/umap_allWT_SP7.png?v=4" width="33%" />

<img src="figures/umap_allWT_CD68.png?v=4" width="33%" /><img src="figures/umap_allWT_ALPL.png?v=4" width="33%" /><img src="figures/umap_allWT_ACAN.png?v=4" width="33%" />

<img src="figures/umap_allWT_MCAM.png?v=4" width="33%" /><img src="figures/umap_allWT_ACTA2.png?v=4" width="33%" /><img src="figures/umap_allWT_NFATC1.png?v=4" width="33%" />

<img src="figures/umap_allWT_IL7R.png?v=4" width="33%" /><img src="figures/umap_allWT_DUSP1.png?v=4" width="33%" /><img src="figures/umap_allWT_MPZ.png?v=4" width="33%" />

<img src="figures/umap_allWT_CD14.png?v=4" width="33%" /><img src="figures/umap_allWT_CALCR.png?v=4" width="33%" /><img src="figures/umap_allWT_AIF1.png?v=4" width="33%" />

<img src="figures/umap_allWT_TAGLN.png?v=4" width="33%" /><img src="figures/umap_allWT_KCNJ8.png?v=4" width="33%" /><img src="figures/umap_allWT_COMP.png?v=4" width="33%" />

<img src="figures/umap_allWT_COL1A1.png?v=4" width="33%" /><img src="figures/umap_allWT_MBP.png?v=4" width="33%" /><img src="figures/umap_allWT_KRT14.png?v=4" width="33%" />

<img src="figures/umap_allWT_JUN.png?v=4" width="33%" /><img src="figures/umap_allWT_PCNA.png?v=4" width="33%" /><img src="figures/umap_allWT_KRT6A.png?v=4" width="33%" />

<img src="figures/umap_allWT_MYH11.png?v=4" width="33%" /><img src="figures/umap_allWT_CD4.png?v=4" width="33%" /><img src="figures/umap_allWT_TP63.png?v=4" width="33%" />

<img src="figures/umap_allWT_KRT5.png?v=4" width="33%" /><img src="figures/umap_allWT_STMN1.png?v=4" width="33%" /><img src="figures/umap_allWT_HIF1A.png?v=4" width="33%" />

<img src="figures/umap_allWT_S100A8.png?v=4" width="33%" /><img src="figures/umap_allWT_CD79A.png?v=4" width="33%" /><img src="figures/umap_allWT_CTSK.png?v=4" width="33%" />

<img src="figures/umap_allWT_COL17A1.png?v=4" width="33%" /><img src="figures/umap_allWT_SOX9.png?v=4" width="33%" /><img src="figures/umap_allWT_CSPG4.png?v=4" width="33%" />

<img src="figures/umap_allWT_CD74.png?v=4" width="33%" /><img src="figures/umap_allWT_KRT16.png?v=4" width="33%" /><img src="figures/umap_allWT_ELANE.png?v=4" width="33%" />

<img src="figures/umap_allWT_KLRD1.png?v=4" width="33%" /><img src="figures/umap_allWT_ITGA6.png?v=4" width="33%" /><img src="figures/umap_allWT_SPP1.png?v=4" width="33%" />

<img src="figures/umap_allWT_DCSTAMP.png?v=4" width="33%" /><img src="figures/umap_allWT_COL2A1.png?v=4" width="33%" />



