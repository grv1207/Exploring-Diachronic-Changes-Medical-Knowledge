import pyemblib
import pickle
url = '/media/gaurav/Elements/Thesis/data/embbedingInitial/__MACOSX/'
#bin_embs = pyemblib.read(url+'embed.csv', mode=pyemblib.Mode.Binary)

#print(bin_embs)
with open(url+'emb.csv','rb') as fout:
    dd = pickle.load(fout)

print(dd)


