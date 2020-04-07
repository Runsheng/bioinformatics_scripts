# Collection of Raw bioinformatics scripts 
### bioinformatics scripts written in python or R. 
* bam2bigGenePred.py: convert the long read RNA-seq mapping bam file to a bigGenePred format, which can be viewed by UCSC browser or by igv
* factor_no.r:  a single r function to parse the factor col and turn them into numbers
* fun_ch.py: one single function to calculate the intersection of a bed coverage file and a rmsk repeat annotation file to return the coverage of the repeat unit (Warning: takes ultra-long time for a large set, use bedtools for large intersection instead)
* gb2gff.py: convert the genebank file to fasta with a gff as annotation
* get_end_count.py: get the frequency of a position as the mapping end of the reads in a bam file 
* line10x.py: duplicate each line of the file to 10 or more times, can be used to fulfill the format need of sspace scaffolder or other wired packages
* N50.py: get the N50 or Nxx for a genome assembly (fasta format), need biopython. 

### folders
1. blastz: The scripts for whole genome alignment with blastz (replaced by lastz now).
2. gbrowser_script: The scripts example used for the loading of WormBase gff to MySQL based Gbrowser database.
3. moleculo_script: The scripts used in the processing of the Illumina Synthetic Long Read (Illumina SLR), previously known as meleculo reads and inherited as 10X genomics long reads.  
4. wormbase: Collections of the script used to parse the dataset from WormBase ftp. 
