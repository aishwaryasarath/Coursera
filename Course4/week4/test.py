import csv
import datetime
import requests

FILE_URL="http://marga.com.ar/employees-with-date.csv"

def get_file_lines(url):

    #print(" In get_file_lines() requesting file")
    response = requests.get(url, stream=True)
    #print("After response")
    lines = []
    for line in response.iter_lines():
        lines.append(line.decode("UTF-8"))
    #print("after for loop in iter_lines")
    return lines

def main():

    data = get_file_lines(FILE_URL)



if __name__ == "__main__":
    main()
