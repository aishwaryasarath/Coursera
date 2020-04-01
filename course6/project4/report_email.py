#!/usr/bin/env python3
import reports
import os
import datetime
import sys
import emails

def process():
  file_names = []
  file_names = os.listdir(os.chdir(os.getcwd()+"/supplier-data/descriptions"))
  summary = ""

  for file in file_names:
    with open(file) as fp:
      for index, line in enumerate(fp):
        if index == 0:
          summary+= "name: " +line.strip()
        elif index == 1:
          summary += "weight: "+ line.strip()
        summary+= "<br/>"

  return summary


def main(argv):
  title = "Processed Update on "
  date = datetime.datetime.now().strftime("%B %d, %Y")
  summary = process()
  reports.generate_report("../../tmp/processed.pdf", title, summary)

  sender = "aishwaryasarath@gmail.com"
  # receiver = "{}@example.com".format(os.environ.get('USER'))
  receiver = "asafsd"
  subject = "Upload Completed - Online Fruit Store"
  body = "All fruits are uploaded to our website successfully. A detailed " \
         "list is attached to this email"
  message = emails.generate(sender, receiver, subject, body,
                            "../../tmp/processed.pdf")
  print(message)
  # emails.send(message)

if __name__ == "__main__":
  main(sys.argv)
