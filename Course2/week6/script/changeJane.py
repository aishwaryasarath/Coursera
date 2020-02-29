#!/usr/bin/env python3

import sys
import subprocess

URL = "/Users/rakeshravindran/PycharmProjects/PythonED/CourseraGoogle/Course2/week6"
filename = sys.argv[1]
new_filename = ""
old_filename = ""
with open(filename, "r+") as file:
    for line in file.readlines():
        old_filename = line.strip()
        new_filename = line.strip().replace("jane","jdoe")
        old_filename = URL+old_filename
        new_filename = URL+new_filename
        subprocess.run(["mv", old_filename,new_filename])



