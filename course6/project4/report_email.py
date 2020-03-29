#!/usr/bin/env python3
import reports
import os
import datetime

file_names = []
file_names = os.listdir(os.chdir(os.getcwd()+"/supplier-data/descriptions"))
summary = ""
title = "Processed Update on "
date = datetime.datetime.now().strftime("%B %d, %Y")
for file in file_names:
  with open(file) as fp:
    for index, line in enumerate(fp):
      if index == 0:
        summary+= "name: " +line.strip()
      elif index == 1:
        summary += "weight: "+ line.strip()
      summary+= "<br/>"
      #summary += "/n"
print(title+date)
print(summary)
print(os.getcwd())
reports.generate_report("../../tmp/processed.pdf",title,summary)

