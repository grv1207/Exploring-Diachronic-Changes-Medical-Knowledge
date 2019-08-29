from argparse import ArgumentParser

import os

import datetime
from gensim import models
from gensim.models import Word2Vec
from gensim.models import KeyedVectors
from gensim.models.callbacks import CallbackAny2Vec
from gensim.test.utils import get_tmpfile
from gensim.parsing.preprocessing import strip_non_alphanum

from commonFunctions import MMOLogger

mylogger = MMOLogger().getLogger(__name__, 'status.log')




def getline(filepath):
    with open(filepath,'r') as fout:
        for line in fout:
            yield(strip_non_alphanum(line).split())




def main(file_path,previous_embedding,word2vec_model,word2vec_model_vectors,
my_size=500, my_window=10, my_min_count=10, my_workers=6, my_sg=1, my_negative=10, my_ns_exponent=0.75, my_alpha=0.025,
         my_min_alpha=0.0001,my_sample=1e-5
         ):
    # loads the pretrained model embedding
    load_start_time = datetime.datetime.now()
    start_word_vectors = KeyedVectors.load_word2vec_format(previous_embedding, binary=False)
    #sentences =  getline(file_path) #[token for token in getline(file_path)]
    load_end_time = datetime.datetime.now()
    mylogger.info('previous embedding loaded in {} time'.format(load_end_time-load_start_time))
    # initialize the model
    train_start_time = datetime.datetime.now()
    model = Word2Vec(size=my_size, window=my_window, min_count=my_min_count, workers=my_workers, sg=my_sg, negative=my_negative, alpha=my_alpha,
                     min_alpha=my_min_alpha, compute_loss=True, sample=my_sample, iter=1, sorted_vocab=1)

    model.build_vocab([token for token in getline(file_path)])
    mylogger.info('vocabulary created')
    # total number of sentences in the corpus
    training_examples_count = model.corpus_count
    mylogger.info('total number of lines %s'%training_examples_count)

    model.build_vocab(list(start_word_vectors.vocab.keys()), update=True, progress_per=1)

    model.intersect_word2vec_format(previous_embedding, binary=False, lockf=1.0)

    model.train([token for token in getline(file_path)], total_examples=training_examples_count, epochs=model.iter)  # chnages

    if not os.path.exists(str(my_min_count)):
        os.makedirs(str(my_min_count))

    mylogger.info('saving in {}.bin'.format(word2vec_model))

    model.save(str(my_min_count)+'/'+word2vec_model+'.bin')
    """
    saved model can be loaded again using :func:`~gensim.models.word2vec.Word2Vec.load`, which supports
        online training and getting vectors for vocabulary words.
    """

    mylogger.info(' saving in {}.vec '.format(word2vec_model_vectors))
    model.wv.save(str(my_min_count)+'/'+word2vec_model_vectors+'.vec')

    """Save KeyedVectors.
    """
    mylogger.info('done with training..., model saved with name {} and vector for model saved with name {} '.format(
        word2vec_model + '.bin', word2vec_model_vectors))
    model.wv.save_word2vec_format(str(my_min_count)+'/'+word2vec_model+'.txt', binary=False)


    train_end_time = datetime.datetime.now()
    mylogger.info('traing for model {} took {} seconds'.format(word2vec_model,train_end_time - train_start_time))


if __name__=='__main__':
    parser = ArgumentParser(description='Word2Vec Embedding creation Concept Biomedical Concepts')
    parser.add_argument('--Initial_Embedding',type=str,help='file for the initial embedding vector',required=True)
    parser.add_argument('--Corpus_file', type=str, help='file of corpus',required=True)
    parser.add_argument('--Model_name', type=str, help='name of the model',required=True)
    #parser.add_argument('--Model_KeyedVector', type=str, help='file of corpus',required=True)
    parser.add_argument('--min_count', type=int, help='minimum word count frequency', default=10)
    parser.add_argument('--workers', type=int, help='no of thread', default=6)
    parser.add_argument('--alpha', type=float, help='learning rate', default=0.025)


    args = parser.parse_args()

    main(file_path=args.Corpus_file,previous_embedding= args.Initial_Embedding,
         word2vec_model=args.Model_name,word2vec_model_vectors=args.Model_name,
         my_min_count=args.min_count, my_workers=args.workers, my_alpha=args.alpha

         )

    #file_path = '/media/gaurav/Elements/Thesis/data/mappedData/mappedData/1865_1980/2s.txt'  # processed_1865_1980
    #previous_embedding = 'pr_embed.txt'
