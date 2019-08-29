"""
This script parses an MMO output that we get from https://mbr.nlm.nih.gov/Download/MetaMapped_Medline/2014/ which is first
partially processed in bash to get utterance and mappings fields

the object of MMO would process each file in given directoy in parallel and would store their result in a dictionary
if the size of dictionary is more than  threshold <3 GB> it would spill out the dictionary in a pickle form
"""
import logging
import pickle
import sys
import os
import subprocess
import multiprocessing as mp
from argparse import ArgumentParser
from macpath import join
from multiprocessing.pool import Pool

"""
Author : Gaurav Vashisth, date:15:05:2018
"""

import re
from collections import OrderedDict
import gzip

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)
hdlr = logging.FileHandler('MMO.log')
formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.INFO)

def parseFile(fileName, src_directory,dest_directory):   #files/processed/ ='/home/gvashisth/thesis/correct_MMO/dest_mapped/'

    if not os.path.isdir(dest_directory):
        os.mkdir(dest_directory)

    pmDict = OrderedDict()
    srcdir = src_directory
    srcFile = srcdir+fileName
    #filL = fileName.split('.')[2]
    dest_file  = '.'.join(fileName.split('.')[:-1])
    destFileURL = dest_directory+dest_file+'.bin'
    logger.info(fileName+'  started')
    if not os.path.isfile(destFileURL):
        with open(srcdir+fileName,'r') as fin:
            for i,line in enumerate(fin):
                if line.startswith('utterance'):
                    line = line.replace('""','\'')
                    lineParts = line.split('"')
                    if (len(lineParts)>1):
                       try:
                            pmID = lineParts[0].split("(")[1].replace("\'","").split('.')[0]
                            sentenceNo = '.'.join(lineParts[0].split("(")[1].replace("\'","").replace(',','').split('.')[1:3])
                            sentence = sentenceNo+' | '+lineParts[1]
                            """
                                take care of offset ofr each concept and store them in a onject
                                create list for concepts"""
                            mainOffset = int(lineParts[2].split(',')[1].split('/')[0])
                            if pmID not in pmDict:
                                pmDict[pmID] = OrderedDict()

                            pmDict[pmID][sentence] = OrderedDict()
                       except Exception as e :
                           logger.error(str(fileName) + ' : ' + str(pmID) + ' : ' + str(e))

                if line.startswith('mappings'):
                    line = line.replace("mappings(","").replace(").",",")
                    try:

                        firstSplit = line.split("map(")[1:]
                        for sublines in firstSplit:
                            secondSplits = sublines.split("ev(")[1:]
                            for parts in secondSplits:
                                """pmDict[pmID][title].append(parts.split(',')[1].replace("\'",""))
                                pmDict[pmID][title].append(parts.split(',')[-4])"""
                                cuiList = parts.split(',')[2].replace("\'", "").split(' ')
                                cuiName = '_'.join(cuiList)
                                #cuiName = re.sub('[^0-9a-zA-Z]+ ', '', cuiName)
                                cuid = parts.split(',')[1].replace("\'","")
                                offset =  hasNumbers(parts.replace('[','').replace(']','').split(',')[int(-4-len(cuiList)+1):][:len(cuiList)],mainOffset,pmID,srcFile)

                                if cuiName not in list(pmDict[pmID][sentence].keys()):
                                    pmDict[pmID][sentence][cuiName] = []
                                    pmDict[pmID][sentence][cuiName].append(cuid)
                                    pmDict[pmID][sentence][cuiName].append(offset)

                    except Exception as e :
                           logger.error(str(fileName) + ' : ' + str(pmID) + ' : ' + str(e))

        logger.info('records: '+fileName+' : '+str(len(pmDict)))





        with open(destFileURL,'wb') as dictOut:
           pickle.dump(pmDict,dictOut,protocol=pickle.HIGHEST_PROTOCOL)
           logger.info(destFileURL+' dumped')

    else:
        logger.info(fileName+' exists ')

    return str(len(pmDict))

def hasNumbers(inputList,mainOffset,pmID, fileName):
    newList = []
    #if pmID=='5807301':
        #print(pmID)
    for sublist in inputList:
        intCount = sublist.replace('/','')
        if len(intCount)>=3:
            if intCount.isdigit():
                subOffsetList = sublist.split('/')
                try:
                    offsetTup =(int(subOffsetList[0]) - mainOffset, int(subOffsetList[1]))
                    newList.append(offsetTup)
                except Exception as e:
                    logger.error(str(fileName)+' : '+str(pmID)+' : '+str(e))
    return newList

def getAllfiles(path):
    """
    returns a list of all files inside a folder
    :param path:
    :return:

    """

    return [ y   for x in (os.walk(path)) for y in x[2]   ]

def  useBash(file):
    folder = '/media/gaurav/Elements/Thesis/data/MMO/CompleteData/'
    folder2 = '/media/gaurav/Elements/Thesis/data/MMO/CompleteData/files/semiprocessed/new/'
    subprocess.call(['./process2.sh', file,folder,folder2])

def uncompressFile(fileName):
    url = '/media/gaurav/Elements/Thesis/data/MMO/CompleteData/'
    newFileName = fileName.replace('.gz','')
    logger.info(fileName+' started')
    with gzip.open(url+fileName, 'rb') as f_in:
        with open(url+newFileName,'wb')as fout :
            for line in f_in:

                fout.write(line)
                fout.write('\n')

    logger.info(fileName+ ' uncompressed to ' +newFileName)
    return  newFileName


def checkfile(file):
    url = '/media/gaurav/Elements/Thesis/data/MMO/CompleteData/'  #/files/processed/'
    file = file.replace('.gz','')
    file = 'sprc.'+file+'.bin'
    destFileURL = url+file
    if os.path.isfile(destFileURL):
        return True
    else:
        return False


def removefile(file):
    os.remove(file)
    logger.info(file+' removed')
    pass


if __name__ == '__main__':

    #url = '/media/gaurav/Elements/Thesis/data/MMO/CompleteData/files/semiprocessed/new/'
    parser = ArgumentParser(description='processes the semi processed files from bash script')
    parser.add_argument('--source_directory', type=str, help='path of source directory', required=True)
    parser.add_argument('--destination_directory', type=str, help='path of source directory', required=True)
    args = parser.parse_args()

    lisOfrawFiles = getAllfiles(args.source_directory)
    list_of_files = []
    for file in lisOfrawFiles:
        #if not bool (checkfile(file)):
            #newfilename = uncompressFile(file)
            #useBash(file)
            #newName = 'sprc.'+file
        #remove .gz from file

        #list_of_files.append(file)
        parseFile(file, src_directory=args.source_directory, dest_directory='/home/gvashisth/thesis/correct_MMO/'+args.destination_directory)
    #list_of_destination = ['/home/gvashisth/thesis/correct_MMO/'+args.destination_directory]*len(lisOfrawFiles)
    #list_of_src = [args.source_directory] * len(lisOfrawFiles)

    #p = Pool(4)
    #p.map_async(parseFile,zip(lisOfrawFiles,list_of_src,list_of_destination)) #(,src_directory=args.source_directory,dest_directory=), zip(list_of_files,)






