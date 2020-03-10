## The scripts used in the processing of the Illumina Synthetic Long Read (Illumina SLR), previously known as meleculo reads and inherited as 10X genomics long reads.  

### Requirement:
1. python 2 (>=2.4)
2. biopython

### Citation:
Li, R., Hsieh, C., Young, A. et al. Illumina Synthetic Long Read Sequencing Allows Recovery of Missing Sequences even in the “Finished” *C. elegans* Genome. Sci Rep 5, 10814 (2015). [https://doi.org/10.1038/srep10814](https://www.nature.com/articles/srep10814)

#### File list
1. phred_to_number.py: write the phred score in fastq file to a new file 
2. phred_normalize.py: for reads with different length, write the normalize phred score to a file with same length bins. 

#### Folders
- runca: the parameters used for the runCA cmd for the celera assembler and mira assembler for the Illumina SLR. 
- bwa_parameter: the parameters used for the bwa mapping for the Illumina SLR
- mnv: the multiple nucleotide variant list, called by CLC genomic workbench 7 or by bcftools 0.5.6
