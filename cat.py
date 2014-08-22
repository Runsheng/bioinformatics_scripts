# 2014/06/19 runsheng
import os
os.system("cat ce100_[0-9].fastq>ce20_0.fastq")
for n in range(1,13):
    print n
    os.system("cat ce100_"+str(n)+"[0-9].fastq>ce20_"+str(n)+".fastq")
    