#sheet_fragmenter.py
from glob import glob
import argparse as pa
import os
from PIL import Image
from time import sleep

parser = pa.ArgumentParser(description = 'First fragments png files horizantally then it go\'s down a row')
parser.add_argument('source_file', help = '')
parser.add_argument('width', type = int, help = '')
parser.add_argument('height', type = int, help = '')
args = parser.parse_args()

def sheet_fragmenter(source_file, width, height):

    row_nr = 0
    images = Image.open(source_file)

    row = height * row_nr
    left = 0
    upper = row
    right = width
    lower = height + row

    image_width = images.size[0]
    image_height = images.size[1]
    number_images = 0

    # Generate files
    while image_width > 0 or image_height > 0:

        row = height * row_nr
        upper = row
        lower = height + row

        generated_name = source_file.split('.')[0]
        generated_name += str(number_images)+'.png'
        print(generated_name)

        # Save file
        images.crop((left, upper, right, lower)).save(generated_name, 'PNG')

        # Debug
        sleep(1)
#print(image_height, image_width)
        #images.crop((left, upper, right, lower)).show()

        # Horizontal steps
        image_width -= width
        left += width
        right += width
        number_images += 1

        # Vertical steps
        if image_width == 0:
            row = height * row_nr
            image_height -= height
            row_nr +=1

            # Reset for itaration on the next row
            left = 0
            right = width
            image_width = images.size[0]

            if image_height < 1:
                break
            else:
                continue

sheet_fragmenter(args.source_file, args.width, args.height)

