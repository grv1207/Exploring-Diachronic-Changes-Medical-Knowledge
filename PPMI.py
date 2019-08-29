import subprocess
from argparse import ArgumentParser
from collections import Counter
from math import sqrt
from random import Random
from docopt import docopt
import commonFunctions as cf
from scipy.sparse import dok_matrix, csr_matrix
from representations.matrix_serializer import save_count_vocabulary, save_matrix, save_vocabulary, load_count_vocabulary
from representations.explicit import PositiveExplicit
import numpy as np
"""
        This snippet is taken from Improving Distributional Similarity with Lessons Learned from Word Embeddings
Omer Levy, Yoav Goldberg, and Ido Dagan. TACL 2015. https://bitbucket.org/omerlevy/hyperwords
"""

class PPMI():

    def __init__(self,corpus_file_name,dict_name,threshold,subsample,window,position,dynamic,delete,pair_file, count_pair_file,pmi_file,neg):
        self.corpus_file_name = corpus_file_name
        self.neg = neg
        self.dict_name = dict_name
        self.thr = threshold
        self.subsample = subsample
        self.win = window
        self.pos = position
        self.dyn = dynamic
        #subsample = float(args['--sub'])
        self.sub = self.subsample != 0
        self.d3l = delete
        self. pair_file = pair_file
        self.count_pair_file = count_pair_file
        self.cds = .75
        self.pmi_file = pmi_file
        self.vocab_dictionary = self._create_vocab()
        self.corpus_size = sum(self.vocab_dictionary.values())

        self.subsample *= self.corpus_size
        self.subsampler = dict([(word, 1 - sqrt(self.subsample / count)) for word, count in self.vocab_dictionary.items() if count > self.subsample])

        cf.saveDictionary(self.vocab_dictionary, self.dict_name.split('/')[0]+'/'+self.dict_name.split('/')[1]+'_vocab.bin')
        self._corpus_2_pairs()

        subprocess.call(['./pairs2counts.sh',self. pair_file,self.count_pair_file ])

        self._counts2Vocab()
        self._counts2PMI()


    def _create_vocab(self):
        vocab = Counter()
        with open(self.corpus_file_name) as f:
            for line in f:
                vocab.update(Counter(line.strip().split()))
        return dict([(token, count) for token, count in vocab.items() if count >= self.thr])



    def _corpus_2_pairs(self):
        """
        :return:
        """
        rnd = Random(17)
        with open(self. pair_file, 'w') as write_file:

            with open(self.corpus_file_name) as f:
                for line in f:

                    tokens = [t if t in self.vocab_dictionary else None for t in line.strip().split()]
                    if self.sub:
                        tokens = [t if t not in self.subsampler or rnd.random() > self.subsampler[t] else None for t in tokens]
                    if self.d3l:
                        tokens = [t for t in tokens if t is not None]

                    len_tokens = len(tokens)

                    for i, tok in enumerate(tokens):
                        if tok is not None:
                            if self.dyn:
                                dynamic_window = rnd.randint(1, self.win)
                            else:
                                dynamic_window = self.win
                            start = i - dynamic_window
                            if start < 0:
                                start = 0
                            end = i + dynamic_window + 1
                            if end > len_tokens:
                                end = len_tokens

                            if self.pos:
                                output = '\n'.join([row for row in
                                                    [tok + ' ' + tokens[j] + '_' + str(j - i) for j in range(start, end) if
                                                     j != i and tokens[j] is not None] if len(row) > 0]).strip()
                            else:
                                output = '\n'.join([row for row in [tok + ' ' + tokens[j] for j in range(start, end) if
                                                                    j != i and tokens[j] is not None] if
                                                    len(row) > 0]).strip()
                            if len(output) > 0:
                                write_file.write(output+'\n')


    def _counts2Vocab(self):
        counts_path = self.count_pair_file
        words = Counter()
        contexts = Counter()
        with open(counts_path) as f:
            for line in f:
                count, word, context = line.strip().split()
                count = int(count)
                words[word] += count
                contexts[context] += count

        words_items = sorted(words.items(), key=lambda x: x[1], reverse=True)
        contexts_items = sorted(contexts.items(), key=lambda x: x[1], reverse=True)

        save_count_vocabulary(counts_path + '.words.vocab', words_items)
        save_count_vocabulary(counts_path + '.contexts.vocab', contexts_items)
        self.words = words
        self.contexts = contexts


    def _counts2PMI(self):

        words = list(self.words.keys())
        contexts = list(self.contexts.keys())
        iw = sorted(words)
        ic = sorted(contexts)
        wi = dict([(w, i) for i, w in enumerate(iw)])
        ci = dict([(c, i) for i, c in enumerate(ic)])

        counts = csr_matrix((len(wi), len(ci)), dtype=np.float32)
        tmp_counts = dok_matrix((len(wi), len(ci)), dtype=np.float32)
        update_threshold = 100000
        i = 0
        with open(self.count_pair_file) as f:
            for line in f:
                count, word, context = line.strip().split()
                if word in wi and context in ci:
                    tmp_counts[wi[word], ci[context]] = int(count)
                i += 1
                if i == update_threshold:
                    counts = counts + tmp_counts.tocsr()
                    tmp_counts = dok_matrix((len(wi), len(ci)), dtype=np.float32)
                    i = 0
        counts = counts + tmp_counts.tocsr()
        pmi = self.calc_pmi(counts, self.cds)

        save_matrix(self.pmi_file, pmi)
        save_vocabulary(self.pmi_file + '.words.vocab', iw)
        save_vocabulary(self.pmi_file + '.contexts.vocab', ic)
        self.explicit = PositiveExplicit(self.pmi_file, normalize=False, neg=self.neg)
        cf.saveDictionary(self.explicit,self.dict_name.split('/')[0]+'/'+self.dict_name.split('/')[1]+'_explicit_ppmi.bin')

        #return counts, iw, ic

    def calc_pmi(self,counts, cds):
        """
        Calculates e^PMI; PMI without the log().
        """
        sum_w = np.array(counts.sum(axis=1))[:, 0]
        sum_c = np.array(counts.sum(axis=0))[0, :]
        if cds != 1:
            sum_c = sum_c ** cds
        sum_total = sum_c.sum()
        sum_w = np.reciprocal(sum_w)
        sum_c = np.reciprocal(sum_c)

        pmi = csr_matrix(counts)
        pmi = self.multiply_by_rows(pmi, sum_w)
        pmi = self.multiply_by_columns(pmi, sum_c)
        pmi = pmi * sum_total
        return pmi

    def multiply_by_rows(self,matrix, row_coefs):
        normalizer = dok_matrix((len(row_coefs), len(row_coefs)))
        normalizer.setdiag(row_coefs)
        return normalizer.tocsr().dot(matrix)

    def multiply_by_columns(self,matrix, col_coefs):
        normalizer = dok_matrix((len(col_coefs), len(col_coefs)))
        normalizer.setdiag(col_coefs)
        return matrix.dot(normalizer.tocsr())












if __name__ =='__main__':
    parser = ArgumentParser(description='PPMI matrix for raw corpus')
    parser.add_argument('--Corpus_file', type=str, help='file of corpus', required=True)
    parser.add_argument('--Model_name', type=str, help='name of the model', required=True)
    parser.add_argument('--min_count', type=int, help='minimum word count frequency', default=5)
    parser.add_argument('--neg_sample', type=int, help='negative sample ', default=10)

    args = parser.parse_args()
    corpus_file = args.Corpus_file #'test'#args['<corpus>']
    thr = args.min_count #1#int(args['--thr'])
    win = 10#int(args['--win'])
    pos = False #args['--pos']
    dyn = True #args['--dyn'
    subsample = 0.00001 #float(args['--sub'])
    sub = subsample != 0
    d3l = True #args['--del']
    #neg = 10

    PPMI(corpus_file_name=corpus_file,dict_name=args.Model_name,threshold=thr,subsample=subsample,
         window=win,position=pos,dynamic=dyn,delete=d3l,pair_file=args.Model_name+'_pair_file', count_pair_file=args.Model_name+'_count_pair_file',pmi_file=args.Model_name+'_pmi',neg=args.neg_sample)