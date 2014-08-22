#2015/06/17
#runsheng
#use an ugly way(os.system) to use the bash script in python
import os
#cat ce20_0.fastq>ce20_s_0.fastq
os.system("cat ce20_0.fastq>ce20_s_0.fastq")
for n in range(1,13):
#cat ce20_s_(n-1).fastq ce20_n.fastq >ce20_s_n.fastq
    os.system("cat ce20_s_"+str(n-1)+".fastq ce20_"+str(n)+".fastq >ce20_s_"+str(n)+".fastq")

#bwa mem -t 15 -k 1000 ../ce1/ce10_ws242.fa ce20_0.fastq>ce20_0.sam
    os.system("bwa mem -t 15 -k 1000 ../ref/ce10_ws242.fa ce20_s_"+str(n)+".fastq>ce20_s_"+str(n)+".sam")
    
#samtools view -bS ce20_0.sam>ce20_0.bam
    os.system("samtools view -bS ce20_s_"+str(n)+".sam>ce20_s_"+str(n)+".bam")
    
#samtools sort ce20_0.bam ce20_0_s
    os.system("samtools sort ce20_s_"+str(n)+".bam ce20_s_"+str(n)+"_s")
    
#bedtools genomecov -ibam ce20_0_s.bam -bga |grep -w 0$ >ce20_0.bed
    os.system("bedtools genomecov -ibam ce20_s_"+str(n)+"_s.bam -bga |grep -w 0$ >ce20_s_"+str(n)+".bed")
    
#cat ce20_0.bed|awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM,"="}'
    bed=open("ce20_s_"+str(n)+".bed").readlines()
    sum=0
    for line in bed:
         sum+=int(line.split("\t")[2])-int(line.split("\t")[1])
    
    print str(n),sum, "="
    
