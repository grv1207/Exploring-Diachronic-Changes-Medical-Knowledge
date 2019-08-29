import numpy
from heapq import nlargest,nsmallest
#from gensim.models import KeyedVectors
from collections import OrderedDict

import pickle
with open('concept_dict.bin','rb') as fin:
    concept_dict = pickle.load(fin)
    
    
def cosine_similarity(vec1,vec2):
    
    """
    returns the normalized cosine similarity between two vector, similar to gensim consine similarity
    """
    return numpy.dot(vec1, vec2)/(numpy.linalg.norm(vec1)* numpy.linalg.norm(vec2))




def cosine_distance_time_periods(first_period,second_period):
    """
    returns two lists, one with biggest changes and another one with least changes  for specific concepts
    """
    similarity_changes= dict()
    for concept_in_first in first_period.vocab:
        if concept_in_first in second_period.vocab:
            vector_in_first = first_period.get_vector(concept_in_first) # first _1865_1980.wv.get_vector("prereplicative")
            vector_in_second = second_period.get_vector(concept_in_first) # second
            similarity_changes[concept_in_first]= cosine_similarity(vector_in_first,vector_in_second)

    return similarity_changes  #, list(nlargest(10, similarity_changes, key=similarity_changes.get)),list(nsmallest(200, similarity_changes, key=similarity_changes.get))


def largest_changes(concept_similarity_dict,threshold=0.49):
    _temp = { k:v for k,v in concept_similarity_dict.items() if v <= threshold }
    return   OrderedDict(sorted(_temp.items(), key=lambda x: x[1]))

def smallest_changes(concept_similarity_dict,threshold=0.49):
    _temp = { k:v for k,v in concept_similarity_dict.items() if v >= threshold }
    return   OrderedDict(sorted(_temp.items(), key=lambda x: x[1]))


def get_neighbours(filename, ll, first_time, second_time, f_name, sec_name):
    with open(filename,'a') as fout:
        
        #for concept in ll:
        concept = ll
            #print(concept)
        if concept in first_time.vocab.keys() and concept in second_time.vocab.keys():

            list_of_concept =first_time.most_similar(concept)
            concept_name = ''
            if concept in concept_dict:
                concept_name = concept_dict[concept]
                #print(concept_name)
            print(concept+'|'+str(concept_name))
            fout.write(str(f_name)+':: '+concept+'|'+str(concept_name))

            for simi_concept in list_of_concept:
                simi_concept_name = ''
                if simi_concept[0] in concept_dict:
                    simi_concept_name = concept_dict[simi_concept[0]]

                print(str(simi_concept) + '|' +str(simi_concept_name))
                fout.write(('|'+str(simi_concept) + '|' +str(simi_concept_name)))

            fout.write('\n')

            list_of_concept_2 = second_time.most_similar(concept)

            fout.write(str(sec_name)+':: '+concept+'|'+str(concept_name))
            print(concept+'|'+str(concept_name))

            for simi_concept_2 in list_of_concept_2:
                simi_concept_name_2 = ''
                if simi_concept_2[0] in concept_dict:
                    simi_concept_name_2 = concept_dict[simi_concept_2[0]]

                print(str(simi_concept_2) + '|' + str(simi_concept_name_2))
                fout.write('|' + str(simi_concept_2) + '|' + str(simi_concept_name_2))
            fout.write('\n')
