#!/usr/bin/env Rscript

library("optparse")

option_list = list(

make_option(c("-f", "--file"), type="character", default=NULL,

help="dataset file name", metavar="character"),

make_option(c("-o", "--out"), type="character", default="out.csv",

help="output file name [default= %default]", metavar="character")

);

opt_parser = OptionParser(option_list=option_list);

opt = parse_args(opt_parser);


if (is.null(opt$file)){

print_help(opt_parser)

stop("At least one argument must be supplied (input file).n", call.=FALSE)

}
score1=read.csv(opt$file, sep=",", header=F)

df=data.frame()
for (i in (1:60)){
    line=c(i, sum(score1$V2>i)) # note the ratio position
    df=rbind(df, line)
}
colnames(df)=c("no", opt$file)

write.csv(df, file=opt$out, row.names=FALSE)
