#!/usr/bin/env python3
import reports
import os
import datatime

file_names = []
file_names = os.listdir(os.chdir(os.getcwd()+"/supp$
summary = ""
title = "Processed update on" datetime. datetime.$
for file in file_names:
  with open(file) as fp:
    for index, line in enumerate(fp):
      if index == 0:
        summary+= line.strip()
      elif index == 1:
        summary += line.strip()
      summary+= "<br/>"
reports.generate_report("/tmp/processed.pdf",title,$


