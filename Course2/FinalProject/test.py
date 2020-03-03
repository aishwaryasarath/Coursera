#!/usr/bin/env python3

import re
import sys
import operator

pattern = r"([ERROR]+|[INFO]+)(.*)(\(\w*\.?\w*\))$"
info_pattern = r"ticky: INFO: ([\w ]*) "
error_pattern = r"ticky: ERROR: ([\w ]*) "
logfile = sys.argv[1]

error_count = {}
user_info_count = {}
user_error_count = {}

with open(logfile) as f:
    for line in f:
        result = re.search(pattern, line)
        # print("result[1]:", result[1])
        # print("result[2]:", result[2])
        # print("result[3]:", result[3])
        #username[name] = username.get(name,0)+1
        error_count[result[2]] = error_count.get(result[2],0)+1
        if result[1] == "INFO":
            user_info_count[result[3]] = user_info_count.get(result[3], 0)+1
        elif result[1] == "ERROR":
            user_error_count[result[3]] = user_error_count.get(result[3], 0)+1

print("error_count: ",sorted(error_count.items(), key=operator.itemgetter(
    1), reverse = True))

print("userinfocount: ",sorted(user_info_count.items(), key=operator.itemgetter(1)))
print("usereroorcount: ", sorted(user_error_count.items(), key=operator.itemgetter(1)))
