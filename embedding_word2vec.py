import os
from argparse import ArgumentParser

import numpy as np
from gensim.models import Word2Vec
from gensim.models.callbacks import CallbackAny2Vec
from gensim.parsing.preprocessing import strip_non_alphanum
from nltk.corpus import stopwords

from commonFunctions import MMOLogger

stopWords = set(stopwords.words('english'))
#mylogger = MMOLogger().getLogger(__name__, 'status.log')


def getline(filepath):
    with open(filepath,'r') as fout:
        for line in fout:
            line_list = strip_non_alphanum(line).split()

            yield([token for token in line_list if token not in stopWords])



class my_callback_each_epoch(CallbackAny2Vec):


    def __init__(self,word2vec_model,my_min_count):
        self.best_loss = np.inf
        self.five_score_list = []
        self.epoch_dict = {}
        self.epoch = 0
        self.word2vec_model = word2vec_model
        self.my_min_count = my_min_count
        self.stop_training = False


    def on_epoch_begin(self, model):
        #print("Epoch #{} start".format(self.epoch))
        if self.stop_training:
            print(self.epoch_dict)
            exit()

    def on_epoch_end(self, model):
        #print("Epoch #{} end".format(self.epoch))
        loss = model.running_training_loss / model.corpus_count
        # print('error : {} '.format(loss))
        print(' present error : {}, best error {} '.format(loss, self.best_loss))
        self.epoch_dict[self.epoch] = loss
        self.epoch += 1
        if loss < self.best_loss:
            self.best_loss = loss
            self.five_score_list = []

            if not os.path.exists(str(self.my_min_count)):
                os.makedirs(str(self.my_min_count))

            print('saving in {}.bin'.format( self.word2vec_model))
            model.save(str(self.my_min_count) + '/' +  self.word2vec_model + '.bin')
            print(' saving in {}.vec '.format( self.word2vec_model))
            model.wv.save(str(self.my_min_count) + '/' +  self.word2vec_model + '.vec')
            model.wv.save_word2vec_format(str(self.my_min_count) + '/' +  self.word2vec_model + '.txt', binary=False)

        else:
            #self.epoch_dict[self.epoch] = loss
            self.five_score_list.append(loss)

        if len(self.five_score_list) ==3:

            self.stop_training = True


def main(file_path, word2vec_model, my_min_count,dimension, negative_size,lr,context_window,worker_thread):
    my_callback = my_callback_each_epoch(word2vec_model, my_min_count)
    model = Word2Vec(sentences= [token for token in getline(file_path)], sg=1,alpha= lr,min_count=my_min_count,size=dimension,sample=0.00001,\
                     negative=negative_size,workers=worker_thread,window=context_window,compute_loss=True,callbacks=[my_callback],iter=100,seed=1)

    #my_callback.epoch_dict.keys()


    #mylogger.info('loss for model {} is {}'.format(word2vec_model,model.get_latest_training_loss()))



if __name__=='__main__':
    parser = ArgumentParser(description='Word2Vec Embedding creation Concept Biomedical Concepts')
    parser.add_argument('--Corpus_file', type=str, help='file of corpus',required=True,default='u_1809_1950')
    parser.add_argument('--dimension', type=int, help='dimension of the embedding', required=True,default=100)
    parser.add_argument('--Model_name', type=str, help='name of the model',required=True,default='1809_1950_100_3_10')
    parser.add_argument('--min_count', type=int, help='minimum word count frequency', default=3)
    parser.add_argument('--negative', type=int, help='negative sample', default=10)
    parser.add_argument('--lr', type=float, help='learning rate', default=.025)
    parser.add_argument('--context_window', type=int, help='learning rate', default=10)
    parser.add_argument('--worker_thread', type=int, help='workerr thread', default=3)


    args = parser.parse_args()

    main(file_path=args.Corpus_file,
         word2vec_model=args.Model_name,
         my_min_count=args.min_count, dimension = args.dimension,negative_size =args.negative, lr = args.lr, context_window = args.context_window, worker_thread = args.worker_thread

         )