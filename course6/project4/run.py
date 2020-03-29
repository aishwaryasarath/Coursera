#! /usr/bin/env python3

import os
import requests

file_names = os.listdir(os.chdir(os.getcwd()+"/supplier-data/descriptions"))
result_json = {}

for file in file_names:
    with open(file) as fp:
        for index, line in enumerate(fp):
            if index == 0:
                result_json["name"] = line.strip()
            elif index == 1:
                result_json["weight"] = int(line.strip().rstrip(" lbs"))
            elif index == 2:
                result_json["description"] = line.strip()
                result_json["image_name"] = file[:-3]+'jpeg'
        print(result_json)


# #! /usr/bin/env python3
#
# import os
# import requests
#
# file_names = []
# result_json = {}
#
# file_names = os.listdir(os.chdir(os.getcwd()+"/supplier-data/descriptions"))
#
# for file in file_names:
#     with open(file) as fp:
#         for index, line in enumerate(fp):
#             if index == 0:
#                 result_json["name"] = line.strip()
#             elif index == 1:
#                 result_json["weight"] = int(line.strip().rstrip(" lbs"))
#             elif index == 2:
#                 result_json["description"] = line.strip()
#                 result_json["image_name"] = file[:-3]+'jpeg'
#         response = requests.post("http://35.223.34.215/fruits/", data = result_json)
#         print(response.status_code)
