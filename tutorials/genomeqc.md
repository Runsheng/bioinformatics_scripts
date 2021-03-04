## The code and protocol used for cell line's genome
#### 0. input files
    FDSW202461999-1r_L2_1.fq.gz
    FDSW202461999-1r_L3_1.fq.gz
    FDSW202461999-1r_L2_2.fq.gz
    FDSW202461999-1r_L3_2.fq.gz
    
#### 1. create an conda enviroument  to run the code
    conda create -n genomeqc
    conda activate genomeqc
##### 2. softwares needed to be installed using "conda install xxxx"
- fastqc: the quality control for fastq file
- trimmomatic: trim adapter and low-quality region from reads
- jellyfish: kmer counting # note the name is "kmer-jellyfish" conda install -c bioconda kmer-jellyfish
- spades: a genome assembler for NGS read, same function as soap-assembler used by the company

#### 3.  merge data from different lanes
    zcat FDSW202461999-1r_L2_1.fq.gz FDSW202461999-1r_L3_1.fq.gz > merge_1.fq
    zcat FDSW202461999-1r_L2_2.fq.gz FDSW202461999-1r_L3_2.fq.gz > merge_2.fq
#### 3.1 QC for fastq (optional)
    ## check the html output 
    fastqc merge_1.fq
    fastqc merge_2.fq

#### 4.Run trimmomatic
##### 4.1 Create a the adaptor fasta file for trimming, use the trim_p_1 and trim_p_2 files for further analysis
```
# adapter.fa
>p7_7UDI501
GATCGGAAGAGCACACGTCTGAACTCCAGTCACGTGGATCAATCTCGTATGCCGTCTTCTGCTTG
>p5
AGATCGGAAGAGCGTCGTGTAGGGAAAGA
```
##### 4.2 run trim using the adapter sequences
    trimmomatic PE -threads 32 -phred33 merge_1.fq merge_2.fq \
	    trim_p_1.fq trim_u_1.fq trim_p_2.fq trim_u_2.fq \
	    ILLUMINACLIP:adapter.fa:2:30:10 LEADING:3 TRAILING:3 SLIDINGWINDOW:4:15 MINLEN:36
	    
#### 5. Run jellyfish with differnt kmers
```
##### k21
jellyfish count -C -m 21 -s 1000000000 -t 10 trim_p*.fq -o read_p.jf
jellyfish histo -t 10 read_p.jf > 21mer.histo
##### k17
jellyfish count -C -m 17 -s 1000000000 -t 10 trim_p*.fq -o read.jf
jellyfish histo -t 10 read.jf > read_k17.histo
##### k26
jellyfish count -C -m 26 -s 1000000000 -t 10 trim_p*.fq -o read.jf
jellyfish histo -t 10 read.jf > read_k26.histo
```

#### 6. draw the kmer figures to estimate the genome size
```R
### run this code in a small windows machine is still OK, just download these .histo file to local machine
library(ggplot2)
library(dplyr)

df17=read.csv("read_k17.histo", sep=" ", header = F)
df17$size="17mer"
df21=read.csv("read_k21.histo", sep=" ", header = F)
df21$size="21mer"
df26=read.csv("read_k26.histo", sep=" ", header = F)
df26$size="26mer"

df=rbind(df17, df22, df26)

# full plot
pdf("kmer.pdf", width=12, height=12)
ggplot(data=df)+geom_point(aes(x=V1, y=V2, color=size))+xlim(0,500)+ylim(0, 1e7)+theme_bw()+xlab("Kmer number")+ylab("Count")
dev.off()

df_max=filter(df, V1>100) %>% group_by(size) %>%
  filter(V2 == max(V2)) %>%
  summarise(V1)

df_start=filter(df, V1>5&V1<80) %>% group_by(size) %>%
  filter(V2 == min(V2)) %>%
  summarise(V1)

# genome size
for (i in c(1,2,3)) {
  kmer=as.character(df_max[i,1])
  #print(as.character(kmer))
  start=as.numeric(filter(df_start, size==kmer)$V1)
  max=as.numeric(filter(df_max, size==kmer)$V1)
  #print(c(start, end, max, kmer))
  df_one=filter(df, size==kmer)
  end=as.numeric(dim(df_one)[1])
  sumall=sum(as.numeric(df_one$V1[start:end]*df_one$V2[start:end]))/max
  print(c(kmer,sumall/1000000))
}
### output for the diploid genome size
### "17mer"            "583 Gb"
### "21mer"            "565.Gb"
### "26mer"            "543.Gb"
```

#### 7. run spades assembler to get the genome
##### please check for cmd detail http://sepsis-omics.github.io/tutorials/modules/spades_cmdline/
spades.py --threads 48 --memory 1400 -1 trim_p_1.fq.gz -2 trim_p_2.fq.gz --careful --cov-cutoff auto -o spadesout

#### 8. Simple parameters for genome
    N50: 6.8 Kb
    Largest contig: 540 Kb
    Total size: 720 Mb (larger than estimattion, indicate insufficient merging of repeats)
    Busco score : 87% (busco4) 
**This genome assembly from spades is just used for survey. A real genome should come from the long reads assembler polished by these short reads.**
