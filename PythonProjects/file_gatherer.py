#file_gatherer.py
from glob import glob
import argparse as pa
import os

parser = pa.ArgumentParser(description = 'Recursively search for files with a certain extention and copy the current map')
parser.add_argument('source', help = 'path of the files')
parser.add_argument('target', help = 'target path')
parser.add_argument('extention', help = 'file extention')
args = parser.parse_args()

def copy_files(source, target, extention):
    ls = glob(source+'**', recursive = True)
    for i in ls:
        if i.endswith(extention):
            os.system('cp -v '+i+" "+target)
            

copy_files(args.source, args.target, args.extention)


