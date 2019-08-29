#!/usr/bin/env bash


: '
echo ' 1809_1970'
python PPMI.py --Corpus_file '/home/gvashisth/experiments/thesis/frames/ws/ws_1809_1970' --Model_name '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model/1809_1970'


#INFO:__main__:1809_1970_fastext_10_300_5.bin,0.5987187357790424,10,10000


echo ' 1971_1975'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_1971_1975 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/1971_1975


#INFO:__main__:1971_1975_fastext_10_300_5.bin,0.578942222778403,10,10000

echo ' 1976_1980'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_1976_1980 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/1976_1980

#INFO:__main__:1976_1980_fastext_10_300_5.bin,0.6070142901089901,10,10000

echo ' 1981_1985'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_1981_1985 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/1981_1985


#INFO:__main__:1981_1985_fastext_10_300_5.bin,0.6173446966154937,10,10000

echo ' 1986_1990'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_1986_1990 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/1986_1990

#INFO:__main__:1986_1990_fastext_10_300_5.bin,0.6078453008666072,10,10000


python significance_test.py --ppm_path 'PPMI_model/1809_1970_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1809_1970_fastext_10_300_5.bin' --vocab_path 'PPMI_model/1809_1970_vocab.bin' --threshold 10000 --neigbours 5

python significance_test.py --ppm_path 'PPMI_model/1971_1975_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1971_1975_fastext_10_300_5.bin' --vocab_path 'PPMI_model/1971_1975_vocab.bin' --threshold 10000 --neigbours 5


python significance_test.py --ppm_path 'PPMI_model/1976_1980_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1976_1980_fastext_10_300_5.bin' --vocab_path 'PPMI_model/1976_1980_vocab.bin' --threshold 10000 --neigbours 5

python significance_test.py --ppm_path 'PPMI_model/1981_1985_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1981_1985_fastext_10_300_5.bin' --vocab_path 'PPMI_model/1981_1985_vocab.bin' --threshold 10000 --neigbours 5

python significance_test.py --ppm_path 'PPMI_model/1986_1990_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1986_1990_fastext_10_300_5.bin' --vocab_path 'PPMI_model/1986_1990_vocab.bin' --threshold 10000 --neigbours 5

python significance_test.py --ppm_path 'PPMI_model/1991_1995_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1991_1995_fastext_10_300_5.bin' --vocab_path 'PPMI_model/1991_1995_vocab.bin' --threshold 10000 --neigbours 5

python significance_test.py --ppm_path 'PPMI_model/1996_2000_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1996_2000_fastext_10_300_5.bin' --vocab_path 'PPMI_model/1996_2000_vocab.bin' --threshold 10000 --neigbours 5

python significance_test.py --ppm_path 'PPMI_model/2001_2005_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2001_2005_fastext_10_300_5.bin' --vocab_path 'PPMI_model/2001_2005_vocab.bin' --threshold 10000 --neigbours 5

python significance_test.py --ppm_path 'PPMI_model/2006_2010_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2006_2010_fastext_10_300_5.bin' --vocab_path 'PPMI_model/2006_2010_vocab.bin' --threshold 10000 --neigbours 5


python significance_test.py --ppm_path 'PPMI_model/2011_2012_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2011_2012_fastext_10_300_5.bin' --vocab_path 'PPMI_model/2011_2012_vocab.bin' --threshold 10000 --neigbours 5


python significance_test.py --ppm_path 'PPMI_model/2013_2015_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2013_2015_fastext_10_300_5.bin' --vocab_path 'PPMI_model/2013_2015_vocab.bin' --threshold 10000 --neigbours 5
'
#########################
:'
python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1809_1970_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1809_1970_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1809_1970_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1971_1975_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1971_1975_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1971_1975_vocab.bin' --threshold 10000 


python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1976_1980_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1976_1980_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1976_1980_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1981_1985_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1981_1985_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1981_1985_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1986_1990_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1986_1990_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1986_1990_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1991_1995_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1996_2000_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2001_2005_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2006_2010_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2006_2010_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2006_2010_vocab.bin' --threshold 10000 


python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2011_2012_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2011_2012_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2011_2012_vocab.bin' --threshold 10000 


python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2013_2015_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2013_2015_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2013_2015_vocab.bin' --threshold 10000 --neigbours 3


python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1991_1995_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1996_2000_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000_vocab.bin' --threshold 10000 

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2001_2005_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005_vocab.bin' --threshold 10000 

'
: '

echo ' 1991_1995'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_1991_1995 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/1991_1995


#INFO:__main__:1971_1975_fastext_10_300_5.bin,0.578942222778403,10,10000

echo ' 1996_2000'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_1996_2000 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/1996_2000



echo ' 2001_2005'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_2001_2005 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/2001_2005

echo ' 2006_2010'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_2006_2010 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/2006_2010


echo ' 2011_2012'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_2011_2012 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/2011_2012

echo ' 2013_2015'
python PPMI.py --Corpus_file /home/gvashisth/experiments/thesis/frames/ws/ws_2013_2015 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model/2013_2015




########## remove duplicate lines
#/home/gvashisth/experiments/thesis/frames/ws
#/mnt/raid0/datasets/gvashisth/thesis/uniq_folder

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_1809_1970 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1809_1970

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_1971_1975 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1971_1975

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_1976_1980 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1976_1980

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_1981_1985 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1981_1985

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_1986_1990 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1986_1990

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_1991_1995 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1991_1995

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_1996_2000 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1996_2000

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_2001_2005 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2001_2005

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_2006_2010 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2006_2010

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_2011_2012 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2011_2012

awk '!x[$0]++' /home/gvashisth/experiments/thesis/frames/ws/ws_2013_2015 > /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2013_2015



#############################################
echo ' 1809_1970'
python PPMI.py --Corpus_file '/mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1809_1970' --Model_name '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1809_1970'


#INFO:__main__:1809_1970_fastext_10_300_5.bin,0.5987187357790424,10,10000


echo ' 1971_1975'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1971_1975 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1971_1975


#INFO:__main__:1971_1975_fastext_10_300_5.bin,0.578942222778403,10,10000

echo ' 1976_1980'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1976_1980 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1976_1980

#INFO:__main__:1976_1980_fastext_10_300_5.bin,0.6070142901089901,10,10000

echo ' 1981_1985'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1981_1985 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1981_1985


#INFO:__main__:1981_1985_fastext_10_300_5.bin,0.6173446966154937,10,10000

echo ' 1986_1990'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1986_1990 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1986_1990


echo ' 1991_1995'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1991_1995 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995


echo ' 1996_2000'
python PPMI.py --Corpus_file/mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1996_2000 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000



echo ' 2001_2005'
python PPMI.py --Corpus_file/mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2001_2005 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005

echo ' 2006_2010'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2006_2010 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2006_2010


echo ' 2011_2012'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2011_2012 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2011_2012

echo ' 2013_2015'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2013_2015 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2013_2015




echo ' 1991_1995'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1991_1995 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995


echo ' 1996_2000'
python PPMI.py --Corpus_file/mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1996_2000 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000




python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1991_1995_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1991_1995_vocab.bin' --threshold 10000 
'


echo ' 1996_2000'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_1996_2000 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000


python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/1996_2000_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/1996_2000_vocab.bin' --threshold 10000 

echo ' 2001_2005'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2001_2005 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005

python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2001_2005_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2001_2005_vocab.bin' --threshold 10000 

echo ' 2013_2015'
python PPMI.py --Corpus_file /mnt/raid0/datasets/gvashisth/thesis/uniq_folder/ws_2013_2015 --Model_name /mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2013_2015


python significance_test.py --ppm_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2013_2015_explicit_ppmi.bin' \
--sgns_path '/mnt/raid0/datasets/gvashisth/thesis/SGNS_trained_model/inc_5_yr/2013_2015_fastext_10_300_5.bin' --vocab_path '/mnt/raid0/datasets/gvashisth/thesis/PPMI_model_uniq/2013_2015_vocab.bin' --threshold 10000