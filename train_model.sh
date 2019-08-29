#!/bin/bash






: '

#1865_1980_10
  python create_embedding.py --Initial_Embedding pr_embed.txt --Corpus_file 'processed_1865_1980'\
 --Model_name '1865_1980_10'  \
  --min_count 10 --workers 10

  # 1981_1990_10
  python create_embedding.py --Initial_Embedding 10/1865_1980_10.txt --Corpus_file '1981_1990'\
 --Model_name '1981_1990_10'  \
  --min_count 10 --workers 10


#  1981_1990_100
  python create_embedding.py --Initial_Embedding '1865_1980_100.txt' --Corpus_file '1981_1990'\
 --Model_name '1981_1990_100'  \
  --min_count 100 --workers 5

# 1981_1990_10
  python create_embedding.py --Initial_Embedding '1865_1980_10.txt' --Corpus_file '1981_1990'\
 --Model_name '1981_1990_10'  \
  --min_count 10 --workers 5


# 1991_1995_100
  python create_embedding.py --Initial_Embedding 1981_1990_100/1981_1990_100.txt --Corpus_file '1991_1995'\
 --Model_name '1991_1995_100'  \
  --min_count 100 --workers 10

 # 1991_1995_10
  python create_embedding.py --Initial_Embedding 1981_1990_10/1981_1990_10.txt --Corpus_file '1991_1995'\
 --Model_name '1991_1995_10'  \
  --min_count 10 --workers 10



    #1996_2000_100
  python create_embedding.py --Initial_Embedding 1991_1995_100/1991_1995_100.txt --Corpus_file '1996_2000'\
 --Model_name '1996_2000_100'  \
  --min_count 100 --workers 10

#1996_2000_10
  python create_embedding.py --Initial_Embedding 1991_1995_10/1991_1995_10.txt --Corpus_file '1996_2000'\
 --Model_name '1996_2000_10'  \
  --min_count 10 --workers 10



   #2001_2003_100
  python create_embedding.py --Initial_Embedding 1996_2000_100/1996_2000_100.txt --Corpus_file '2001_2003'\
 --Model_name '2001_2003_100'  \
  --min_count 100 --workers 10

#2001_2003_10
  python create_embedding.py --Initial_Embedding 1996_2000_10/1996_2000_10.txt --Corpus_file '2001_2003'\
 --Model_name '2001_2003_10'  \
  --min_count 10 --workers 10



   #2004_2006_100
  python create_embedding.py --Initial_Embedding 2001_2003_100/2001_2003_100.txt --Corpus_file '2004_2006'\
 --Model_name '2004_2006_100'  \
  --min_count 100 --workers 10

#2004_2006_10
  python create_embedding.py --Initial_Embedding 2001_2003_10/2001_2003_10.txt --Corpus_file '2004_2006'\
 --Model_name '2004_2006_10'  \
  --min_count 10 --workers 10


   #2007_2009_100
  python create_embedding.py --Initial_Embedding 2004_2006_100/2004_2006_100.txt --Corpus_file '2007_2009'\
 --Model_name '2007_2009_100'  \
  --min_count 100 --workers 10


#2007_2009_10
  python create_embedding.py --Initial_Embedding 2004_2006_10/2004_2006_10.txt --Corpus_file '2007_2009'\
 --Model_name '2007_2009_10'  \
  --min_count 10 --workers 10




   #2010_2011_100
  python create_embedding.py --Initial_Embedding 100/2007_2009_100.txt --Corpus_file '2010_2011'\
 --Model_name '2010_2011_100'  \
  --min_count 100 --workers 10


#2010_2011_10
  python create_embedding.py --Initial_Embedding 10/2007_2009_10.txt --Corpus_file '2010_2011'\
 --Model_name '2010_2011_10'  \
  --min_count 10 --workers 10


   #2012_2016_100
  python create_embedding.py --Initial_Embedding 100/2010_2011_100.txt --Corpus_file '2012_2016'\
 --Model_name '2012_2016_100'  \
  --min_count 100 --workers 10


#2012_2016_10
  python create_embedding.py --Initial_Embedding 10/2010_2011_10.txt --Corpus_file '2012_2016'\
 --Model_name '2012_2016_10'  \
  --min_count 10 --workers 10
   ####################################################################################################################
   ####### new training ###############################################################################################
   ###################################################################################################################
'


: '
##############################done ########################################################
#1865_1980_10
  python create_embedding.py --Initial_Embedding pr_embed.txt --Corpus_file 'processed_1865_1980'\
 --Model_name '1865_1980_10'  \
  --min_count 10 --workers 10
  #####################################################################
  '

  # 1981_1990_10
  python create_embedding.py --Initial_Embedding 10/1865_1980_10.txt --Corpus_file '1981_1990'\
 --Model_name '1981_1990_10'  \
  --min_count 10 --workers 10

 # 1991_1995_10
  python create_embedding.py --Initial_Embedding 10/1981_1990_10.txt --Corpus_file '1991_1995'\
 --Model_name '1991_1995_10'  \
  --min_count 10 --workers 10



#1996_2000_10
  python create_embedding.py --Initial_Embedding 10/1991_1995_10.txt --Corpus_file '1996_2000'\
 --Model_name '1996_2000_10'  \
  --min_count 10 --workers 10




#2001_2003_10
  python create_embedding.py --Initial_Embedding 10/1996_2000_10.txt --Corpus_file '2001_2003'\
 --Model_name '2001_2003_10'  \
  --min_count 10 --workers 10


#2004_2006_10
  python create_embedding.py --Initial_Embedding 10/2001_2003_10.txt --Corpus_file '2004_2006'\
 --Model_name '2004_2006_10'  \
  --min_count 10 --workers 10



#2007_2009_10
  python create_embedding.py --Initial_Embedding 10/2004_2006_10.txt --Corpus_file '2007_2009'\
 --Model_name '2007_2009_10'  \
  --min_count 10 --workers 10


#2010_2011_10
  python create_embedding.py --Initial_Embedding 10/2007_2009_10.txt --Corpus_file '2010_2011'\
 --Model_name '2010_2011_10'  \
  --min_count 10 --workers 10



#2012_2016_10
  python create_embedding.py --Initial_Embedding 10/2010_2011_10.txt --Corpus_file '2012_2016'\
 --Model_name '2012_2016_10'  \
  --min_count 10 --workers 10
