from glob import glob
import os
import argparse
from time import sleep

parser = argparse.ArgumentParser(description =
"Changes names of files with the same name without changing the extention names")

#parser.add_argument("to_change", help = "")
parser.add_argument("original", help = "")
parser.add_argument("new_name", help = "")
args = parser.parse_args()


def fu(original, new_name):
    ignore_list = ["PNG", "png", "import"]
    #if glob("*").__contains__(to_change) == True:
    #print(type(glob("*")))
    os.system("cp -r {} {}".format(original, new_name))
    sleep(0.4)
    
    for i in glob(new_name+"/*"):
    #for i in glob(original+"/*"):
        #if i.startswith(to_change):
        if len(i.split(".")) > 1:
            extention = i.split(".")[1]
            if extention in ignore_list:
                pass
            else:
                changed_name = new_name+"."+extention
                #os.system("mv {} {}".format(i, changed_name))
                os.system("mv {} {}".format(i, new_name+"/"+changed_name))

#                os.system("sed -i 's/{0}/{1}/' {2}".format(original[:-1], new_name, new_name+"/"+new_name+".tscn"))
#                os.system("sed -i 's/{0}/{1}/' {2}".format(original[:-1]+".gd",
            print(changed_name)
#                          new_name+".gd", new_name+"/"+new_name+".tscn"))
    return original, new_name

    #os.system("sed -i 's/{0}/{1}/g' {2}".format(original+".gd",
            #new_name+".gd", new_name+"/"+new_name+".tscn"))

#    else:
#        print("invalid filename")
#        return

original, new_name = fu(args.original, args.new_name)

# For some reason escape character needs to be escaped "\\b to set boundery"
os.system("sed -i 's/\\b{0}/{1}/g' {2}".format(original, new_name, new_name+"/"+new_name+".tscn"))

