#!/usr/bin/env python3

import re
import csv
import sys
import operator
import itertools
import string
from collections import defaultdict

pattern = r"([ERROR]+|[INFO]+)(.*)(\(\w*\.?\w*\))$"
logfile = sys.argv[1]

error = {}
per_user = defaultdict(lambda: defaultdict(dict))

with open(logfile) as f:
    for line in f:
        result = re.search(pattern, line)
        error[result[2].strip()] = error.get(result[2].strip(), 0) + 1
        if result[1] == "INFO":
            per_user[result[3]]["INFO"] = per_user[result[3]].get("INFO",
                                                                  0)+1
        elif result[1] == "ERROR":
            per_user[result[3]]["ERROR"] = per_user[result[3]].get("ERROR",
                                                                 0) + 1

error_sorted = sorted(error.items(), key=operator.itemgetter(1), reverse=True)
per_user_sorted = sorted(per_user.items(), key=operator.itemgetter(0))
fields_err = ['Error', 'Count']
fileds_user = ['Username', 'INFO', 'ERROR']

with open('error_message.csv', 'w', newline='') as error_csv:
    writer = csv.DictWriter(error_csv,fields_err)
    writer.writeheader()
    for key,value in error_sorted:
        writer.writerow({'Error':key, 'Count':value})

with open('user_statistics.csv', 'w', newline='') as user_stat_csv:
    writer_u = csv.DictWriter(user_stat_csv, fileds_user)
    writer_u.writeheader()
    for user,val in per_user_sorted:
        val.setdefault('INFO', 0)
        val.setdefault('ERROR', 0)
        writer_u.writerow({'Username': user.strip("(").strip(")"),
                           'INFO':val['INFO'], 'ERROR':val['ERROR'] })


# for user,val in per_user_sorted:
#     val.setdefault('INFO',0)
#     val.setdefault('ERROR',0)
#     print(user.strip("(").strip(")"), val['INFO'], val['ERROR'])
    # if user =="(bpacheco)":
        #print(user,val['INFO'],val['ERROR'])
        #print(type(val['INFO']))



