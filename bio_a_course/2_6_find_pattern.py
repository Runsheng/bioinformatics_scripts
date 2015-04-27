def PatternCount(Text, Pattern):
    count= 0
    for i in range (0,(len(Text)-len(Pattern))):
        if Text[i:(i+len(Pattern))] == Pattern:
            count=count+1
            print i+1,
    return count
    
a="GATATATGCATATACTT"
b="ATAT"

PatternCount(a,b)