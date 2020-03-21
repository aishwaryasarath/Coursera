#! /usr/bin/env python3

import os
import requests

file_names = []
result_json = {}

file_names = os.listdir(os.chdir("/data/feedback"))

for file in file_names:
    with open(file) as fp:
        for index, line in enumerate(fp):
           # print(index,line)
            if index == 0:
                result_json["title"] = line.strip()
            elif index == 1:
                result_json["name"] = line.strip()
            elif index == 2:
                result_json["date"] = line.strip()
            elif index == 3:
                result_json["feedback"] = line.strip()
#        print(result_json)
        response = requests.post("http://34.70.251.223/feedback/", data = result_json)
        print(response.status_code)
#        print(response.text[:300])

