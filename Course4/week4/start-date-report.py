#1.Download the file only once from the URL.
#2.Pre-process it so that the same calculation doesn't need to be done over
# and over again. This can be done in two ways. You can choose any one of them:
#a)To create a dictionary with the start dates and then use the data in the
# dictionary instead of the complicated calculation.
#b)To sort the data by start_date and then go date by date.
#!/usr/bin/env python3
import csv
import datetime
import requests
import operator

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_start_date():

    year = int(input('Enter a value for the year: '))
    month = int(input('Enter a value for the month: '))
    day = int(input('Enter a value for the day: '))
    return datetime.datetime(year, month, day)

def get_file_lines(url):

    response = requests.get(url, stream=True)
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    return lines

    #return saved values from csv

def get_same_or_newer(start_date,data):

    #data = get_file_lines(FILE_URL)
    reader = csv.reader(data[1:])
    reader = sorted(reader, key = operator.itemgetter(3))
    #print("After reader")
    min_date = datetime.datetime.today()
    min_date_employees = []
    for row in reader:
        row_date = datetime.datetime.strptime(row[3], '%Y-%m-%d')
        if row_date < start_date:
            continue
        if row_date < min_date:
            min_date = row_date
            min_date_employees = []
        if row_date == min_date:
            min_date_employees.append("{} {}".format(row[0], row[1]))
    return min_date, min_date_employees


def list_newer(start_date,data):
    while start_date < datetime.datetime.today()
        start_date, employees = get_same_or_newer(start_date,data)
        print("Started on {}: {}".format(start_date.strftime("%b %d, %Y"), employees))
        start_date = start_date + datetime.timedelta(days=1)

def main():

    start_date = get_start_date()
    data = get_file_lines(FILE_URL)

    list_newer(start_date,data)


if __name__ == "__main__":
    main()
