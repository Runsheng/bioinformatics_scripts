# -*- coding: utf-8 -*-
def FrequentWords(Text, k):
    """Input: A string Text and an integer k.
    Output: All most frequent k-mers in Text.
    The input Text is a string and k is an int"""
    FrequentPatterns=[]
    Count=[] # a list that contains all the count for a kmer
    for i in range(0,(len(Text)-k)):
        Pattern = Text[i:(i+k)]
        count=PatternCount(Text, Pattern)
        print count
        Count.append(count) # ie: kmer=3, then scan every 3 k mer inside all the sequence
    print Count
    maxCount=max(Count) #maxCount ← maximum value in array Count
    print maxCount
    for i in range(0, (len(Text)-k)): # for i ← 0 to |Text| − k
        if Count[i] == maxCount:
            FrequentPatterns.append(Text[i:(i+k)]) #add Text(i, k) to FrequentPatterns
        FrequentPatterns=list(set(FrequentPatterns))
    return FrequentPatterns  #remove duplicates from FrequentPatterns

def PatternCount(Text, Pattern):
    """"The pattern of the motif for the mismatches, 
    The input Text is a string and Pattern is also a string
    """
    count= 0
    for i in range (0,(len(Text)-len(Pattern))):
        if Text[i:(i+len(Pattern))] == Pattern:
            count=count+1
    return count

#example
a="CAATGCTGGTAAGGGTGGGCGCGGTAAGGGGTAAGGATAACTCCATAACTCCATAACTCCCAATGCTATAACTCCGGTAAGGGAAGGGAAGTGGGCGCGTGGGCGCGGTAAGGGGTAAGGATAACTCCCAATGCTGTGGGCGCGGTAAGGGAAGGGAAATAACTCCGTGGGCGCCAATGCTGTGGGCGCGGTAAGGGTGGGCGCGGTAAGGATAACTCCCAATGCTGTGGGCGCATAACTCCCAATGCTGTGGGCGCGGTAAGGGAAGGGAAGTGGGCGCATAACTCCGGTAAGGGTGGGCGCGAAGGGAAGGTAAGGCAATGCTATAACTCCCAATGCTATAACTCCCAATGCTGTGGGCGCCAATGCTGTGGGCGCCAATGCTGGTAAGGCAATGCTGGTAAGGGGTAAGGATAACTCCGAAGGGAAGAAGGGAACAATGCTCAATGCTATAACTCCCAATGCTGAAGGGAAGTGGGCGCGAAGGGAAGTGGGCGCGGTAAGGCAATGCTGTGGGCGCCAATGCTCAATGCTCAATGCTCAATGCTCAATGCTCAATGCTGAAGGGAAGAAGGGAAGTGGGCGCATAACTCCATAACTCCATAACTCCGAAGGGAAGAAGGGAAGGTAAGGATAACTCCATAACTCCGTGGGCGCATAACTCCGAAGGGAAGAAGGGAAGAAGGGAAATAACTCCCAATGCTGAAGGGAAGTGGGCGCGAAGGGAACAATGCTCAATGCTATAACTCCGTGGGCGCCAATGCTGTGGGCGCCAATGCTGAAGGGAAGTGGGCGCGGTAAGGGTGGGCGCATAACTCCATAACTCCGGTAAGGGGTAAGGATAACTCCGTGGGCGCGTGGGCGC"
b=11
print FrequentWords(a,b)
