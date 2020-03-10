#2015/06/17
#runsheng

import os
for n in [10,20,30,40,50,60,70,80,90,100,110,120,130]:
#bwa mem -t 15 -k 1000 ../ce1/ce10_ws242.fa ce100_0.fastq>ce100_0.sam
    os.system("bwa mem -t 15 -k 1000 ../ce1/ce10_ws242.fa ce100_"+str(n)+".fastq>ce100_"+str(n)+".sam")
    
#samtools view -bS ce100_0.sam>ce100_0.bam
    os.system("samtools view -bS ce100_"+str(n)+".sam>ce100_"+str(n)+".bam")
    
#samtools sort ce100_0.bam ce100_0_s
    os.system("samtools sort ce100_"+str(n)+".bam ce100_"+str(n)+"_s")
    
#bedtools genomecov -ibam ce100_0_s.bam -bga |grep -w 0$ >ce100_0.bed
    os.system("bedtools genomecov -ibam ce100_"+str(n)+"_s.bam -bga |grep -w 0$ >ce100_"+str(n)+".bed")
    
#cat ce100_0.bed|awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM,"="}'
    #bed=open("ce100_"+str(n)+".bed").readlines()
    #sum=0
    #for line in bed:
    #     sum+=int(line.split("\t")[2])-int(line.split("\t")[1])
    
    #print str(n),sum, "="
    