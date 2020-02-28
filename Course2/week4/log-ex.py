#!/usr/bin/env python3
import sys
import re


logfile = sys.argv[1]
username = {}
with open(logfile) as f:
    for line in f:
        if "CRON" not in line:
            continue
        pattern = r"USER \((\w+)\)$"
        result = re.search(pattern, line)
        if result is None: #to check that we actually got a match to our
            # regular expression
            continue
        name = result[1]
        username[name] = username.get(name,0)+1
print(username)
        #print(result[1])
        #print(line.strip())

