# -*- coding: utf-8 -*-
complement_map = dict(zip("acgtACGTNn-","tgcaTGCANn-"))
def reverse_complement(sequence):
    """due to the complement_map, 
    the symbol such as \n and something else is illegal
    the input need to be pure sequence"""
    complement=[]
    for s in sequence:
        complement.append(complement_map[s])
    reverse=''.join(reversed(complement))
    return reverse
#example
a=open("dataset_3_2.txt").readlines()
print reverse_complement(a[0].strip())