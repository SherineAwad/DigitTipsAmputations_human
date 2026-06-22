

splitpipe_ref_hg38:
	split-pipe --mode mkref --genome_name hg38 \
	--fasta /rds/user/sa941/hpc-work/data/REFERENCES/GRCh38.primary_assembly.genome.fa \
	--genes /rds/user/sa941/hpc-work/data/REFERENCES/gencode.v49.primary_assembly.annotation.gtf \
	--output_dir ./splitpipe_ref_hg38 \
	--nthreads 12




parse_matrices: WT47 

WT%:
	split-pipe --mode all --until_step dge \
		--fq1 /rds/project/rds-ivbvKVT8GC0/parse_scRNA/SLX-27704.ParseWT$*.23J7JTLT4.s_6.r_1.fq.gz \
		--fq2 /rds/project/rds-ivbvKVT8GC0/parse_scRNA/SLX-27704.ParseWT$*.23J7JTLT4.s_6.r_2.fq.gz \
		--genome_dir /rds/project/rds-ivbvKVT8GC0/parse_scRNA/splitpipe_ref_hg38 \
		--output_dir  /rds-d7/user/sa941/hpc-work/data/parse_scRNAseq/WT$* \
   		--kit WT --chemistry 3 --nthreads 12 \
		--sample Uninjured A1:A12 --sample 3d B1:B12 --sample 6d C1:C12 --sample 9d D1:D12
