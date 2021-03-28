import os
from glob import glob
import argparse as pa

# Argparse
description = "create tar takes file extention as argument / for directorys"
parser = pa.ArgumentParser(description = description)
parser.add_argument('file_type', help = 'file type')
args = parser.parse_args()

def create_tar(file_type):
    list_of_files = glob("*"+file_type)
    print (list_of_files)
    confirm = input('Do you want to create tar file ? y/n ')
    if confirm == "y":
        for i in list_of_files:
            if i.endswith("/"):
                t = i.split(file_type)
                os.system("tar -cvf {} {}".format(t[0]+".tar", i))
            else:
                os.system("tar -cvf {} {}".format(i+".tar", i))

def hasupper(word):#used in functions below
    for i in word:
        if i.isupper():
            return True

def lowercase_files_with_extentions():
    extention_list = ["zip", "tar", "gz", "gif", "mp3", "mp4", "sh", "html"]
    lsdir = os.listdir()
    files_to_process = []
    for i in lsdir:
        if hasupper(i) == True : 
            for e in extention_list:
                if i.endswith(e):
                    files_to_process.append(i)

    [print(i) for i in files_to_process]
    confirm = input('Do you want to lowercase file ? y/n ')
    if confirm == "y":
        [os.rename(i, i.lower()) for i in files_to_process]

create_tar(args.file_type)
lowercase_files_with_extentions()

