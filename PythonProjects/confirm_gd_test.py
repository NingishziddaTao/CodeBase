
#confirm_gd_test.py
import argparse as pa
import os

description = " This program only runs from the home directory and\n the target needs the be inside the GodotEngineProjects folder"

parser = pa.ArgumentParser(description = description)
parser.add_argument('target', help = 'target path')
args = parser.parse_args()

def replace_files(target):
    print(target)

    assert target.startswith("GodotEngineProjects"), "Not a gd project"
    assert target != "GodotEngineProjects/", "Cannot overwrite the target"
                
    a = input("do you want to overwrite "+target+"? \ntype y:\nenter to cancel: \n>>> ")
    if a != "y":
        return
    else:
        os.system("rsync -r -v --delete ~/go/ "+target)

replace_files(args.target)


