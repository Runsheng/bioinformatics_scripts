# R 3.02
# to parse the factor col and turn them into numbers
# before: f1,f2,f1,f3,this,no...
# after: 1,2,1,3,4,5...
# runsheng 2014/05/23

factor_no <- function(dataline) {
    fa = factor(dataline)
    # these print is just for debug, that sometime the col of a dataframe can not be translated correctly.
    print("length=")
    print(length(fa))
    print("levels=")
    print(length(levels(fa)))
    v=vector()
     
    for (name in fa) {
        for (i in 1:length(levels(fa))) {
            if (name == levels(fa)[i]) {
                v=append(v,i) 
            }
        }
    }
    return(v)
}

#example
#ccc=factor_no(rmsk_chrIII$repClass) # input is the dataline of a col in dataframe
#rmsk_chrIII$repClass_no=ccc # add this col back to the dataframe
