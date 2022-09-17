### The survey for the L and S phase modification change using nanopore reads
#### 1. samples
    1. 20201124_L: E.coli K12 in L phase
    2. 20201124_S: E.coli K12 in S phase
#### 2. basecalling using high accurate guppy basecaller (V.4.1.2, report to be 94% for RNA reads)
Note: This is suggested to run only with GPU server (the server used to run the sequencing has a GPU)
```bash
guppy_basecaller -i . \
    -r -c rna_r9.4.1_70bps_hac.cfg \
    -s  ./fastq_guppy42 \
    --builtin_scripts 1 \
    -x auto
```
#### 3. read summary
   1. read number: 339715 (L); 68102 (S)
   2. read yield: 63M (L); 10 M (S)
   3. read distribution peaked at around 90 and 150 nt 
      ![read length distribution (bin=10 bp)](.\figs\Ecoli_lenplot.svg){:height="200px" width="200px"}

#### 4. read mapping
   1. reference used: GCF_000005845.2_ASM584v2 from [NCBI genome portal](https://www.ncbi.nlm.nih.gov/genome/167?genome_assembly_id=161521) or [NCBI FTP](https://ftp.ncbi.nlm.nih.gov/genomes/all/GCF/000/005/845/GCF_000005845.2_ASM584v2/)
   2. mapping is done by using [minimap2](https://github.com/lh3/minimap2) and count is done by htseq-count
        ```
        minimap2 -ax map-ont -t 32  \
            GCF_000005845.2_ASM584v2_genomic.fna  \
            20201124_L.fastq >L.sam
        samtools sort L.sam > L.bam
        samtools index L.bam
        htseq-count --format=sam --stranded="no" \
            L.sam \
            GCF_000005845.2_ASM584v2_genomic.gff \
            --type=gene --idattr=Name >L.count
        ```
   3. check the expression with S.count and L.count (count2.xlsx)

Term | L |S
------------ | -------------|-------------
__no_feature  |  133 | 2
__ambiguous    | 1557| 38
__too_low_aQual |503283| 32634
__not_aligned   |241147 | 61307
__alignment_not_unique |0 | 0
mapped to rRNAs | 


#### 5. The RNA methylation calling 
halted, tombo run finsihed, megalodon run(self model) finished with warning. 
epinano/nanocompare failed 