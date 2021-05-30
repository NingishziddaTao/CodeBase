#file_gatherer.py
from glob import glob
import argparse as pa
import os

parser = pa.ArgumentParser(description = 
'Search for files from the current directory with a certain extention in a recursive directory structure 
and copy the files into target directory ')

#parser.add_argument('source', help = 'path of the files')
parser.add_argument('target', help = 'target path')
parser.add_argument('extention', help = 'file extention')
args = parser.parse_args()

#def copy_files(source, target, extention):
def copy_files(target, extention):
    ls = glob('**', recursive = True)
    for i in ls:
        if i.endswith(extention):
            os.system('cp -v '+i+" "+target)

copy_files(args.extention, args.target)
#copy_files(args.source, args.target, args.extention)


