#!/usr/bin/env python3
import requests

url = "http://localhost/upload/"
with open('/usr/share/apache2/icons/icon.sheet.pnh','rb') as opened:
    r = requests.post(url,files ={'file':opened})
