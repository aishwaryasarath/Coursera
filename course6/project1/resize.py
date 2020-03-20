#!/usr/bin/env python3

import os
import sys
from PIL import Image


old_path = os.getcwd() + "/opt/icons/"
new_path = os.getcwd() + "/images/"

for image in os.listdir(path):

    if '.' not in image[0]:
        img = Image.open(old_path + image)
        img.rotate(-90).resize((128, 128)).convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
        img.close()

    # infile = path+item
    # if os.path.isfile(infile):
    #     f, e = os.path.splitext(infile)
    #     outfile = f + ".JPEG"
    #     if infile != outfile:
    #         try:
    #             Image.open(infile).rotate(90).resize((128, 128)).convert("RGB").save(url+item[:-4]+'jpeg', "JPEG", quality=100)
    #         except IOError:
    #             print("Cannot convert", infile)

