#!/usr/bin/env python
import subprocess
import os


src = "data/prod/"
dest = "data/prod_backup/"

print(os.getcwd())

subprocess.call(["rsync", "-arq", src, dest])







