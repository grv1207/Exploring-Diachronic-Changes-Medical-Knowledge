from argparse import ArgumentParser

from gensim.models import FastText
from gensim.parsing.preprocessing import strip_non_alphanum

from commonFunctions import MMOLogger

mylogger = MMOLogger().getLogger(__name__, 'fasttext_status.log')



def getline(filepath):
    with open(filepath,'r') as fout:
        for line in fout:
            yield(strip_non_alphanum(line).split())

def main(file_path, my_min_count, my_workers):

    model = FastText([token for token in getline(file_path)], size=4, window=10, min_count=5, iter=10,size=500)

    pass


if __name__=='__main__':
    parser = ArgumentParser(description='Fasttext framework for Embedding from Biomedical Concepts')
    #parser.add_argument('--Initial_Embedding',type=bool,help='file for the initial embedding vector',required=True)
    parser.add_argument('--Corpus_file', type=str, help='file of corpus',required=True)
    parser.add_argument('--Model_name', type=str, help='name of the model',required=True)
    #parser.add_argument('--Model_KeyedVector', type=str, help='file of corpus',required=True)
    parser.add_argument('--min_count', type=int, help='minimum word count frequency', default=10)
    parser.add_argument('--workers', type=int, help='no of thread', default=10)
    #parser.add_argument('--alpha', type=float, help='learning rate', default=0.025)


    args = parser.parse_args()

    main(file_path=args.Corpus_file,
         my_min_count=args.min_count, my_workers=args.workers

         )