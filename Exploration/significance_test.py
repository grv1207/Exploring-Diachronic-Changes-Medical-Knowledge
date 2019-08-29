from argparse import ArgumentParser
from numba import jit
import os
os.environ["MKL_NUM_THREADS"] = "7" 
os.environ["NUMEXPR_NUM_THREADS"] = "7" 
os.environ["OMP_NUM_THREADS"] = "7" 
from gensim.models import FastText,Word2Vec
#import comman_function_analysis as cf
import commonFunctions as cff
import pickle
import numpy as np
from scipy.sparse import dok_matrix, csr_matrix
import scipy.stats
from commonFunctions import MMOLogger
from collections import Counter
mylogger = MMOLogger().getLogger(__name__, 'significance_test_result.log')

from matplotlib import pyplot as plt
import matplotlib.lines as mlines
import matplotlib.transforms as mtransforms



@jit
def get_PPMI_score(pmi_dict, word1, word2):
    """
    return a ppmi score for  word1 and word2 present in pmi_dict
    """
    return pmi_dict.represent(word1).dot(pmi_dict.represent(word2).T)[0, 0]


"""
def get_coo(sgns, pmdict, word_list, top_neighbors):
    #pers_score = []
    cosine_list = []
    ppmi_list = []
    for word in word_list:
        neighbor_list = sgns.wv.most_similar(word, topn=top_neighbors)
        for neighbor in neighbor_list:
            ppm_score = get_PPMI_score(pmdict, word, neighbor[0])
            ppmi_list.append(ppm_score)
            cosine_list.append(neighbor[1])
        # print('{}, {} , {},  {}'.format(word,neighbor[0],neighbor[1],ppm_score))
        #pers_score.append((scipy.stats.pearsonr(cosine_list, ppmi_list)))

    return cosine_list,ppmi_list
"""
@jit
def get_concept_neighbor(sgns_model, word, negbhour_length):
    neghbour_list = []
    for neighbour in sgns_model.wv.most_similar(word, topn=500):
        if neighbour[0].startswith('C') and len(neighbour[0])==8:
            #print(neighbour)
            neghbour_list.append((neighbour[0],neighbour[1]))
        if len(neghbour_list) == negbhour_length:
            break
    return neghbour_list

def get_coo(sgns, pmdict, word_list, top_neighbors):
    #pers_score = []
    avg_cosine,avg_pmi= [],[]
    for word in word_list:
        neighbor_list = get_concept_neighbor(sgns,word, negbhour_length=top_neighbors)
        #sgns.wv.most_similar(word, topn=top_neighbors)
        cosine_list = []
        ppmi_list = []
        if len(neighbor_list)== top_neighbors:
            
            for neighbor in neighbor_list:
                ppm_score = get_PPMI_score(pmdict, word, neighbor[0])
                ppmi_list.append(ppm_score)
                cosine_list.append(neighbor[1])
            avg_cosine.append(np.mean(cosine_list))
            avg_pmi.append(np.mean(ppmi_list))
        else:
            avg_cosine.append(0)
            avg_pmi.append(0)
        # print('{}, {} , {},  {}'.format(word,neighbor[0],neighbor[1],ppm_score))
        #pers_score.append((scipy.stats.pearsonr(cosine_list, ppmi_list)))

    return avg_cosine,avg_pmi




def main(ppm_path,sgns_path,vocab_path,neigbours_list,threshold):
    name = vocab_path.split('/')[1].split('_vocab.bin')[0]
    with open(ppm_path, 'rb') as fout:
        ppmi_matrix = pickle.load(fout)
   
    sgns_model = FastText.load_fasttext_format(sgns_path)

    with open(vocab_path,'rb') as fout:
        vocab_dict = pickle.load(fout)
    ordered_dict = Counter(vocab_dict)
    
    common_concepts = list(set(sgns_model.wv.vocab.keys()).intersection(set([k for k,v in ordered_dict.most_common(threshold)])))

    #list_greater_threshold = #np.array([k for k,v in vocab_dict.items() if v >= threshold and k in common_concepts])
    print('length of common_concept {}'.format(len(common_concepts)))

    pers_score = []
    concept_list = np.random.choice(common_concepts, size=threshold, replace=False)
    for nn in neigbours_list:
        cosine_list, ppmi_list = get_coo(sgns_model, ppmi_matrix, concept_list, nn)
        pers_score.append(scipy.stats.pearsonr(cosine_list, ppmi_list))
        #print('epoch {} pearson score : {}'.format(i,pers_score[i]))


    #dt = np.dtype('float,float')
    #np.savetxt('significance_test_result/'+sgns_path.split('/')[-1],np.array(pers_score,dtype=dt),delimiter=',')

    #print('Average correlation for {} is {} with {} neighbours and for top {} concepts'.format(sgns_path.split('/')[-1], np.mean([_score[0] for _score in pers_score]),neigbours,threshold))
        mylogger.info("{},{},{},{},{}".format(sgns_path.split('/')[-1],np.mean([_score[0] for _score in pers_score]),np.mean([_score[1] for _score in pers_score]),nn,threshold))
        fig, ax = plt.subplots()
        ax.scatter (cosine_list,ppmi_list,s=2 )
        line = mlines.Line2D([0, 1], [0, 1], color='red')
        transform = ax.transAxes
        line.set_transform(transform)
        ax.add_line(line)
        plt.xlabel("SGNS similarity score ({})".format(name))
        plt.ylabel("PPMI similarity score ({})".format(name))
        plt.show()
        plt.savefig('SGNS-PPMI-{}-{}'.format(nn,name))
        
if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--ppm_path', type=str, help='file of ppmi matrix', required=True)
    parser.add_argument('--sgns_path', type=str, help='file of the SGNS model', required=True)
    parser.add_argument('--vocab_path', type=str, help='file of vocabulary dictionary', required=True)
    parser.add_argument('--threshold', type=int, help='Top N concept, default is 10,000', default=10000)
    #parser.add_argument('--neigbours', type=int, help='no of Top K neighbours', default=10)
    args = parser.parse_args()
    #fil_logger = MMOLogger().getLogger(__name__, 'significance_test_result/'+ args.sgns_path.split('/')[-1].split('.')[0]+'.log' ) args.neigbours
    main(args.ppm_path,args.sgns_path,args.vocab_path,[10,5,3], args.threshold)

