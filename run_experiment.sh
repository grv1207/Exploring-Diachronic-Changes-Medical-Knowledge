#!/bin/bash



echo ' u_1809_1990'

./fastText/fasttext skipgram -input u_1809_1990 -output SGNS_trained_model/u_1809_1950_fastext_10_200_1 -maxn 0 -verbose 2 -dim 200 -ws 10 -minCount 3 -neg 10

echo ' u_1991_2015'
./fastText/fasttext skipgram -input u_1991_2015 -output SGNS_trained_model/u_1809_1950_fastext_10_200_15 -maxn 0 -verbose 2 -dim 200 -ws 10 -minCount 3 -neg 10
