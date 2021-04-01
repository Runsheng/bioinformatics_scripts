# Collection of Raw bioinformatics scripts 
### bioinformatics scripts written in python or R. 
* bam2bigGenePred.py: convert the long read RNA-seq mapping bam file to a bigGenePred format, which can be viewed by UCSC browser or by igv
* bedin.py: generate a bed file using the genome with given bin size
* fa_merge.py: merge the contigs from different assembly, and remove the duplicated ones
* factor_no.r:  a single r function to parse the factor col and turn them into numbers
* faSize.py: minmic the function of kent UCSC "faSize -detailed" function
* fun_ch.py: one single function to calculate the intersection of a bed coverage file and a rmsk repeat annotation file to return the coverage of the repeat unit (Warning: takes ultra-long time for a large set, use bedtools for large intersection instead)
* gb2gff.py: convert the genbank file to fasta with a gff as annotation
* get_end_count.py: get the frequency of a position as the mapping end of the reads in a bam file 
* get_near_ref.py: a pipeline script to select the nearest sequencing among a givien reference using NGS or long read sequencing data. Do the mapping and counting for different chromosomes (contigs), select the most mapped one as nearest one. Works well for small genome like viral genomes or plasmids. 
* line10x.py: duplicate each line of the file to 10 or more times, can be used to fulfill the format need of sspace scaffolder or other wired packages
* minirna.py: raw pipeline script. Do minimap mapping for all fastq files in a folder. 
* N50.py: get the N50 or Nxx for a genome assembly (fasta format), need biopython. 
* phred_per_read.py: get the table from fastq as "readname phred_score_per_nucl phred_average" 
* runiter.py: A general runner for the functions require multiple rounds of iteration, like genome polishing
* runpara.py: A general para runner for the functions with fixed input file types and parameters


### folders
1. blastz: The scripts for whole genome alignment with blastz (replaced by lastz now).
2. gbrowser_script: The scripts example used for the loading of WormBase gff to MySQL based Gbrowser database.
3. moleculo_script: The scripts used in the processing of the Illumina Synthetic Long Read (Illumina SLR), previously known as meleculo reads and inherited as 10X genomics long reads.  
4. wormbase: Collections of the script used to parse the dataset from WormBase ftp. 
