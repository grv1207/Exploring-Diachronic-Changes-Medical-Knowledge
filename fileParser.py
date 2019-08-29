import pickle
import xml.etree.ElementTree as ET

import os

import logging
import multiprocessing as mp

import sys

logging.basicConfig(level=logging.ERROR)
fileParserlog = logging.getLogger(__name__)
hdlr = logging.FileHandler('../Downloader/log/2017.log')
formatter = logging.Formatter('%(asctime)s %(message)s')
hdlr.setFormatter(formatter)
fileParserlog.addHandler(hdlr)
fileParserlog.setLevel(logging.INFO)
import traceback

def processFile(fileURL):
    # fileURL = filePair[0]
    # print(fileURL)
    destinationFolder = '../Downloader/processedData/'

    fileName = fileURL.split('/')[-1].split('.')[0] + '.txt'
    destFileURL = destinationFolder + fileName
    if not os.path.isfile(destFileURL):
        try:
            tree = ET.parse(fileURL)  # ET.parse('../Downloader/2012/medline12n0655.xml') #
            root = tree.getroot()
            with open(destFileURL, 'w') as fout:
                for child in root:
                    pubID = child.find("MedlineCitation").find("PMID").text
                    if (pubID == '45519'):
                        print(pubID)
                    country = ''
                    affliationtext = ''
                    try:
                        # articleTile = child.find("MedlineCitation").find("Article").find("ArticleTitle").text
                        pubYear = child.find('PubmedData').find('History').find('PubMedPubDate').find('Year').text

                        if child.find("MedlineCitation").find("MedlineJournalInfo").find(
                                "Country") is not None:

                            country = child.find("MedlineCitation").find("MedlineJournalInfo").find(
                                "Country").text.lower()

                            contryList = country.split(' ')
                            if len(contryList) > 1:
                                country = '_'.join(map(str, contryList)).lower()



                        if child.find("MedlineCitation").find("Article").find("AuthorList") is not None and child.find(
                                "MedlineCitation").find("Article").find("AuthorList").find(
                                "Author") is not None and child.find("MedlineCitation").find("Article").find(
                            "AuthorList").find("Author").find(
                            "AffiliationInfo")is not None  and child.find("MedlineCitation").find("Article").find("AuthorList").find(
                                "Author").find("AffiliationInfo").find("Affiliation") is not None:

                            lastTest = child.find("MedlineCitation").find("Article").find("AuthorList").find(
                                "Author").find("AffiliationInfo").find("Affiliation").text.split(',')[
                                -1].lstrip().rstrip()
                            affList = lastTest.lower().split(' ')
                            if len(affList) > 1:
                                affliationtext = u'_'.join(map(str, affList)).strip()
                            else:

                                affliationtext = lastTest.lower().replace('.', '').strip()

                        fout.write('{0}|{1}|{2}|{3}'.format(str(pubID), str(pubYear), str(country), str(
                            affliationtext).lstrip().rstrip()))
                        fout.write('\n')

                    except Exception as e :

                        fileParserlog.error('file: %s, pmID: %s, e: %s, line: %s '%(fileURL, pubID,str(e),sys.exc_info()[-1].tb_lineno ))

            fileParserlog.info(' ' + fileName + ' dumped')
        except Exception :

            fileParserlog.error(fileURL + str(sys.exc_info()[-1].tb_lineno))

    else:
        fileParserlog.info(' ' + fileName + ' exits!!')


def getFolderList(mainFolderURL):
    """
    This functions returns all the subfolders in a particular folder(Downloader/data)
    :param mainFolderURl: url of data folder
    :return: list of all the subfolder in Downloader/data
    """

    return [x[1] for x in (os.walk(mainFolderURL))][0]


def convertUTF8toASCII(yyFolder, mainFolderURL='../Downloader'):
    """
    This function take year, extract all files in the that year and give it to processFile, which saves the processed file in processData folder in Downloader folder
    :param listOfFolders:
    :param mainFolderURL:
    :return:
    """
    fileParserlog.info(str(yyFolder) + ' started')
    listOfFiles = [x[2] for x in (os.walk(mainFolderURL + '/' + str(yyFolder)))][0]


    srcfileList = []
    for file in listOfFiles:
        srcfileList.append(mainFolderURL+'/'+str(yyFolder)+'/'+file)

    

    p = mp.Pool(2)
    p.map(processFile, srcfileList)

    # for i in range(3,10):

    #processFile(fileURL='/media/gaurav/Elements/Thesis/src/ExtractDataFromMedline/Downloader/2017/medline17n000'+str(i)+'.xml')
    #processFile(fileURL='/media/gaurav/Elements/Thesis/src/ExtractDataFromMedline/Downloader/2017/medline17n0002.xml')
    fileParserlog.info(str(yyFolder)+' Done')

    pass


def main():
    # subfolderList = getFolderList(mainFolderURL='../Downloader/data')
    subfolderList = [2017]
    for yy in subfolderList:
        convertUTF8toASCII(yy)


if __name__ == '__main__':
    main()
