#!/usr/bin/env python3
import requests
import os

path = os.getcwd() + '/supplier-data/images/'

url = "http://localhost/upload/"
for image in os.listdir(path):
  with open(path+image, 'rb') as opened:
      r = requests.post(url, files={'file': opened})
