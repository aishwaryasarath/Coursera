import csv


input_file = csv.DictReader(open("people.csv"))
for row in input_file:
    print(dict(row))
