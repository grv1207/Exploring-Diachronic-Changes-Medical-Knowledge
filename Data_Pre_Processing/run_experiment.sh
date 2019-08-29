#!/bin/bash

###SGNS



# for 10 window size -epoch

 for i in  `seq 5 1 10`; do
	    echo 'runing for itertaion ': $i	
            #echo item: $i
            mkdir SGNS_trained_model/'5_yr_'$i 


../fastText/fasttext skipgram -input ../frames/1809_1970 -output SGNS_trained_model/'5_yr_'$i/1809_1970_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5

../fastText/fasttext skipgram -input ../frames/1971_1975 -output SGNS_trained_model/'5_yr_'$i/1971_1975_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/1809_1970_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/1976_1980 -output SGNS_trained_model/'5_yr_'$i/1976_1980_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/1971_1975_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/1981_1985 -output SGNS_trained_model/'5_yr_'$i/1981_1985_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/1976_1980_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/1986_1990 -output SGNS_trained_model/'5_yr_'$i/1986_1990_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/1981_1985_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/1991_1995 -output SGNS_trained_model/'5_yr_'$i/1991_1995_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/1986_1990_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/1996_2000 -output SGNS_trained_model/'5_yr_'$i/1996_2000_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/1991_1995_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/2001_2005 -output SGNS_trained_model/'5_yr_'$i/2001_2005_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/1996_2000_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/2006_2010 -output SGNS_trained_model/'5_yr_'$i/2006_2010_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/2001_2005_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/2011_2012 -output SGNS_trained_model/'5_yr_'$i/2011_2012_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/2006_2010_fastext_10_300_5.vec

../fastText/fasttext skipgram -input ../frames/2013_2015 -output SGNS_trained_model/'5_yr_'$i/2013_2015_fastext_10_300_5 -maxn 0 -verbose 2 -dim 300 -ws 10 -minCount 5 -neg 10 -thread 5 -pretrainedVectors SGNS_trained_model/'5_yr_'$i/2011_2012_fastext_10_300_5.vec



	echo 'done itertaion ': $i 
        done


