
#sheet_creator.py
from glob import glob
import argparse as pa
import os
from PIL import Image

working_directory = "/sdb2/FrameTemp/"

parser = pa.ArgumentParser(description = 'Takes file name and destination to create a sheet out of multiple png files')
parser.add_argument('file_name', help = 'Name of the created file')
parser.add_argument('destination', help = 'Write to file location')
args = parser.parse_args()

def create_sheet(file_name, destination):

    load_files = glob(working_directory+'*.png*')
    images = map(Image.open, load_files)
    drawing = map(Image.open, load_files)

    # Get files image sizes for some reason this lin destroys images in images
    widths, heights = zip(*(i.size for i in images))

    # Setup for lining images horizontaly
    total_width = sum(widths)
    max_height = max(heights)

    # Use pil to generate rectangle for new image
    new_im = Image.new('RGBA', (total_width, max_height), (0, 0, 0, 0))

    # Paste images into rectangle
    x_offset = 0
    for im in drawing:
      new_im.paste(im, (x_offset,0), mask = im)
      x_offset += im.size[0]

    # Check image
#new_im.show()
    while 1:

#        answer = input('do you want to save this image? y or n \n>>> ')
#        if answer == 'y':

        new_im.save(destination+file_name+'.png', 'PNG')
        print(file_name+".png was saved into "+destination)
        print("and removed files")
        os.system("rm "+working_directory+"*.png")
        break

#        else:
#            break

create_sheet(args.file_name, args.destination)


