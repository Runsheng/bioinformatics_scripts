#2015/06/17
#runsheng
import os
#cat ce20_12.fastq>ce20_s_12.fastq
os.system("cat ce20_13.fastq>ce20_s_13.fastq")
for n in [13,12,11,10,9,8,7,6,5,4,3,2,1]:
    print n
#cat ce20_s_(n-1).fastq ce20_n.fastq >ce20_s_n.fastq
    os.system("cat ce20_s_"+str(n)+".fastq ce20_"+str(n-1)+".fastq >ce20_s_"+str(n-1)+".fastq")

#bwa mem -t 1 -k 1000 ../ce1/ce10_ws242.fa ce20_s_11.fastq>ce20_s_11.sam
    os.system("bwa mem -t 15 -k 1000 ../ref/ce10_ws242.fa ce20_s_"+str(n-1)+".fastq>ce20_s_"+str(n-1)+".sam")
    
#samtools view -bS ce20_0.sam>ce20_0.bam
    os.system("samtools view -bS ce20_s_"+str(n-1)+".sam>ce20_s_"+str(n-1)+".bam")
    
#samtools sort ce20_0.bam ce20_0_s
    os.system("samtools sort ce20_s_"+str(n-1)+".bam ce20_s_"+str(n-1)+"_s")
    
#bedtools genomecov -ibam ce20_0_s.bam -bga |grep -w 0$ >ce20_0.bed
    os.system("bedtools genomecov -ibam ce20_s_"+str(n-1)+"_s.bam -bga |grep -w 0$ >ce20_s_"+str(n-1)+".bed")
    
#cat ce20_0.bed|awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM,"="}'
    bed=open("ce20_s_"+str(n-1)+".bed").readlines()
    sum=0
    for line in bed:
         sum+=int(line.split("\t")[2])-int(line.split("\t")[1])
    
    print str(n-1),sum, "="
    