import os

def hasupper(word): # used in functions below
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

lowercase_files_with_extentions()
