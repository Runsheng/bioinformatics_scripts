#index the ref
#bwa index ce10_ws242.fa
#use different fastq file
echo "start"
#cat 1.fastq 2.fastq > s2.fastq
#cat s2.fastq 3.fastq > s3.fastq
#cat s3.fastq 4.fastq > s4.fastq
#cat s4.fastq 5.fastq > s5.fastq
#cat s5.fastq 6.fastq > s6.fastq
#cat s6.fastq 7.fastq > s7.fastq
#cat s7.fastq 8.fastq > s8.fastq
#cat s8.fastq 9.fastq > s9.fastq
#cat s9.fastq 10.fastq > s10.fastq
#cat s10.fastq 11.fastq > s11.fastq
#cat s11.fastq 12.fastq > s12.fastq
#cat s12.fastq 13.fastq > s13.fastq
#cat s13.fastq 14.fastq > s14.fastq
#cat s14.fastq 15.fastq > s15.fastq
#cat s15.fastq 16.fastq > s16.fastq
#cat s16.fastq 17.fastq > s17.fastq
#cat s17.fastq 18.fastq > s18.fastq
#cat s18.fastq 19.fastq > s19.fastq
echo "file done"
#make the alignment with 15 node, 1000bp mapping, gap consistence 15000bp(useful in variation call)
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa 1.fastq > ce1_1.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s2.fastq > ce1_2.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s3.fastq > ce1_3.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s4.fastq > ce1_4.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s5.fastq > ce1_5.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s6.fastq > ce1_6.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s7.fastq > ce1_7.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s8.fastq > ce1_8.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s9.fastq > ce1_9.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s10.fastq > ce1_10.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s11.fastq > ce1_11.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s12.fastq > ce1_12.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s13.fastq > ce1_13.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s14.fastq > ce1_14.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s15.fastq > ce1_15.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s16.fastq > ce1_16.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s17.fastq > ce1_17.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s18.fastq > ce1_18.sam
bwa mem -t 15 -k 1000 -w 15000 ce10_ws242.fa s19.fastq > ce1_19.sam
echo "bwa done"
#convert sam to bam
samtools view -bS ce1_1.sam > ce1_1.bam
samtools view -bS ce1_2.sam > ce1_2.bam
samtools view -bS ce1_3.sam > ce1_3.bam
samtools view -bS ce1_4.sam > ce1_4.bam
samtools view -bS ce1_5.sam > ce1_5.bam
samtools view -bS ce1_6.sam > ce1_6.bam
samtools view -bS ce1_7.sam > ce1_7.bam
samtools view -bS ce1_8.sam > ce1_8.bam
samtools view -bS ce1_9.sam > ce1_9.bam
samtools view -bS ce1_10.sam > ce1_10.bam
samtools view -bS ce1_11.sam > ce1_11.bam
samtools view -bS ce1_12.sam > ce1_12.bam
samtools view -bS ce1_13.sam > ce1_13.bam
samtools view -bS ce1_14.sam > ce1_14.bam
samtools view -bS ce1_15.sam > ce1_15.bam
samtools view -bS ce1_16.sam > ce1_16.bam
samtools view -bS ce1_17.sam > ce1_17.bam
samtools view -bS ce1_18.sam > ce1_18.bam
samtools view -bS ce1_19.sam > ce1_19.bam
echo "bam done"
#sort the bam file
# note the ".bam" will be added to the filename, and the output file will be ce_bwa_ws220_s.bam
samtools sort ce1_1.bam ce1_1_s
samtools sort ce1_2.bam ce1_2_s
samtools sort ce1_3.bam ce1_3_s
samtools sort ce1_4.bam ce1_4_s
samtools sort ce1_5.bam ce1_5_s
samtools sort ce1_6.bam ce1_6_s
samtools sort ce1_7.bam ce1_7_s
samtools sort ce1_8.bam ce1_8_s
samtools sort ce1_9.bam ce1_9_s
samtools sort ce1_10.bam ce1_10_s
samtools sort ce1_11.bam ce1_11_s
samtools sort ce1_12.bam ce1_12_s
samtools sort ce1_13.bam ce1_13_s
samtools sort ce1_14.bam ce1_14_s
samtools sort ce1_15.bam ce1_15_s
samtools sort ce1_16.bam ce1_16_s
samtools sort ce1_17.bam ce1_17_s
samtools sort ce1_18.bam ce1_18_s
samtools sort ce1_19.bam ce1_19_s
echo "sort done"
# bam file 0 coverage region
bedtools genomecov -ibam ce1_1_s.bam -bga |grep -w 0$ >ce1_1_s_0_coverage.bed
bedtools genomecov -ibam ce1_2_s.bam -bga |grep -w 0$ >ce1_2_s_0_coverage.bed
bedtools genomecov -ibam ce1_3_s.bam -bga |grep -w 0$ >ce1_3_s_0_coverage.bed
bedtools genomecov -ibam ce1_4_s.bam -bga |grep -w 0$ >ce1_4_s_0_coverage.bed
bedtools genomecov -ibam ce1_5_s.bam -bga |grep -w 0$ >ce1_5_s_0_coverage.bed
bedtools genomecov -ibam ce1_6_s.bam -bga |grep -w 0$ >ce1_6_s_0_coverage.bed
bedtools genomecov -ibam ce1_7_s.bam -bga |grep -w 0$ >ce1_7_s_0_coverage.bed
bedtools genomecov -ibam ce1_8_s.bam -bga |grep -w 0$ >ce1_8_s_0_coverage.bed
bedtools genomecov -ibam ce1_9_s.bam -bga |grep -w 0$ >ce1_9_s_0_coverage.bed
bedtools genomecov -ibam ce1_10_s.bam -bga |grep -w 0$ >ce1_10_s_0_coverage.bed
bedtools genomecov -ibam ce1_11_s.bam -bga |grep -w 0$ >ce1_11_s_0_coverage.bed
bedtools genomecov -ibam ce1_12_s.bam -bga |grep -w 0$ >ce1_12_s_0_coverage.bed
bedtools genomecov -ibam ce1_13_s.bam -bga |grep -w 0$ >ce1_13_s_0_coverage.bed
bedtools genomecov -ibam ce1_14_s.bam -bga |grep -w 0$ >ce1_14_s_0_coverage.bed
bedtools genomecov -ibam ce1_15_s.bam -bga |grep -w 0$ >ce1_15_s_0_coverage.bed
bedtools genomecov -ibam ce1_16_s.bam -bga |grep -w 0$ >ce1_16_s_0_coverage.bed
bedtools genomecov -ibam ce1_17_s.bam -bga |grep -w 0$ >ce1_17_s_0_coverage.bed
bedtools genomecov -ibam ce1_18_s.bam -bga |grep -w 0$ >ce1_18_s_0_coverage.bed
bedtools genomecov -ibam ce1_19_s.bam -bga |grep -w 0$ >ce1_19_s_0_coverage.bed
echo "0 coverage done"
#bam file all coverage region
bedtools genomecov -ibam ce1_1_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_2_s.bam -bga >ce1_2_s_all_coverage.bed
bedtools genomecov -ibam ce1_3_s.bam -bga >ce1_3_s_all_coverage.bed
bedtools genomecov -ibam ce1_4_s.bam -bga >ce1_4_s_all_coverage.bed
bedtools genomecov -ibam ce1_5_s.bam -bga >ce1_5_s_all_coverage.bed
bedtools genomecov -ibam ce1_6_s.bam -bga >ce1_6_s_all_coverage.bed
bedtools genomecov -ibam ce1_7_s.bam -bga >ce1_7_s_all_coverage.bed
bedtools genomecov -ibam ce1_8_s.bam -bga >ce1_8_s_all_coverage.bed
bedtools genomecov -ibam ce1_9_s.bam -bga >ce1_9_s_all_coverage.bed
bedtools genomecov -ibam ce1_10_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_11_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_12_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_13_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_14_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_15_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_16_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_17_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_18_s.bam -bga >ce1_1_s_all_coverage.bed
bedtools genomecov -ibam ce1_19_s.bam -bga >ce1_1_s_all_coverage.bed
echo "all coverage done"

cat  ce1_1_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_2_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_3_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_4_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_5_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_6_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_7_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_8_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_9_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_10_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_11_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_12_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_13_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_14_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_15_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_16_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_17_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_18_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'
cat  ce1_19_s_0_coverage.bed | awk -F'\t' 'BEGIN{SUM=0}{ SUM+=$3-$2 }END{print SUM}'




