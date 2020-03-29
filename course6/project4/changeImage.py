#!/usr/bin/env python3
import os
from PIL import Image

path = os.getcwd() + '/supplier-data/images/'
for image in os.listdir(path):
  if  image.endswith('tiff'):
    img = Image.open(path+image)
    img.resize((600,400)).convert("RGB").save(path+image[:4]+'jpeg', 'jpeg')
    img.close() 
