## The scripts example used for the loading of WormBase gff to MySQL based Gbrowser database

### Requirement:
1. python 2 (>=2.4)
2. biopython

### file list
1. chrname.py: change the name of "chrX" to "X" to fit the WormBase format
2. fasta2gff.py: generate a gff file used for the loading of the fasta file
3. gff_select.py: select coding genes from a large gff file
4. gff_type.py: report the line count for different types of a gff file  
5. scan_aa.py: scan if the first amino acid in the protein sequence is "M", and report the numbers of the "full-length" proteins (starts with "M"). Could be useful for some gene predictors which tends to report incomplete gene models. 
6. gff2fasta.py: get the coding sequence and the protein sequencing from the maker GFF file