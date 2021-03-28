#!/usr/bin/env python3

#start_godot.py
import argparse
from os import *

#parser = argparse.ArgumentParser(description = "")
#parser.add_argument('project_dir', help = "")
#args = parser.parse_args()

#def open_project(project_dir):
def open_project():
    #chdir(project_dir)
    chdir("/sdb2/go")
    system("godot -e")

#open_project(args.project_dir)
open_project()

