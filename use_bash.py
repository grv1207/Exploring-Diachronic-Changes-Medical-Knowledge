import gzip
import subprocess
from argparse import ArgumentParser
import commonFunctions as cf

mylogger = cf.MMOLogger().getLogger(__name__, 'use_bash.log')




def  useBash(file,dest_directory):
    folder = '/mnt/hdd/datasets/gvashisth/'
    subprocess.call(['./process2.sh', file,folder,dest_directory])

if __name__ == '__main__':
    parser = ArgumentParser(description='processes the raw file in -gz format')
    parser.add_argument('--range', type=str, help='range of file to process i:e from 100-199,200-299', required=True)
    parser.add_argument('--destination_directory', type=str, help='path of destination directory', required=True)
    #parser.add_argument('--source_directory', type=str, help='path of src directory', required=True)
    args = parser.parse_args()

    lisOfrawFiles = cf.getAllfiles('/mnt/hdd/datasets/gvashisth/',startStr='text.out_'+args.range)
    list_of_files = []

    for file in lisOfrawFiles:
        #file = 'text.out_'+str(index)+'.gz'
        #uncompressed_file = uncompressFile('/mnt/hdd/datasets/gvashisth/'+file)

        useBash(file, dest_directory='/mnt/hdd/datasets/gvashisth/'+args.destination_directory)