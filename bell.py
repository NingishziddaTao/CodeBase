from playsound import playsound
from time import sleep
import argparse
import os

parser = argparse.ArgumentParser(description = "")
parser.add_argument("seconds", help = "")
args = parser.parse_args()

def fu(seconds):
    s = int(seconds)

    while True:
        sleep(1)
        if s > 0:
            s -= 1
            print(s)
        if s == 0:
            playsound('/sdb2/PythonProjects/bell')
            os.system("exit")
            return
        pass

fu(args.seconds)
