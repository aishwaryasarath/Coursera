#!/usr/bin/env python3

import os
from PIL import Image

old_path = os.getcwd() + '/images/'
new_path = os.getcwd()+ '/images/'

for image in os.listdir(old_path):
        if '.' not in image[0]:
                img = Image.open(old_path + image)
                img.resize((128, 128)).convert("RGB").save(new_path + image.split('.')[0], 'jpeg')
                img.close()

