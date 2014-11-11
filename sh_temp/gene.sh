echo "gene"
bedtools intersect -a gene.bed -b ce2.5x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a gene.bed -b ce5x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a gene.bed -b ce12x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a gene.bed -b ce24x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a gene.bed -b ce2.5x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a gene.bed -b ce5x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a gene.bed -b ce12x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a gene.bed -b ce24x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l
echo "rmsk"
bedtools intersect -a rmsk.bed -b ce2.5x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a rmsk.bed -b ce5x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a rmsk.bed -b ce12x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a rmsk.bed -b ce24x_celera_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a rmsk.bed -b ce2.5x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a rmsk.bed -b ce5x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a rmsk.bed -b ce12x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l
bedtools intersect -a rmsk.bed -b ce24x_mira_0_coverage.bed -wa |sort -n|uniq|wc -l