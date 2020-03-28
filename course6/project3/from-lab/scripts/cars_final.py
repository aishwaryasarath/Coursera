#!/usr/bin/env python3

import json
import locale
import sys
import operator
import itertools
import reports
import emails
import os

def load_data(filename):
  """Loads the contents of filename as a JSON file."""
  with open(filename) as json_file:
    data = json.load(json_file)
  return data


def format_car(car):
  """Given a car dictionary, returns a nicely formatted name."""
  return "{} {} ({})".format(
      car["car_make"], car["car_model"], car["car_year"])


def process_data(data):
  """Analyzes the data, looking for maximums.

  Returns a list of lines that summarize the information.
  """
  locale.setlocale(locale.LC_ALL, 'en_US.UTF8')
  max_revenue = {"revenue": 0}
  max_sales = {"total_sales": 0}
  sales_year = {}
  for item in data:
    # Calculate the revenue generated by this model (price * total_sales)
    # We need to convert the price from "$1234.56" to 1234.56
    item_price = locale.atof(item["price"].strip("$"))
    item_revenue = item["total_sales"] * item_price
    if item_revenue > max_revenue["revenue"]:
      item["revenue"] = item_revenue
      max_revenue = item
    # TODO: also handle max sales
    if item["total_sales"] > max_sales["total_sales"]:
      max_sales["total_sales"] = item["total_sales"]
      max_sales = item
    # TODO: also handle most popular car_year
    year_key = item["car"]["car_year"]
    sales_year[year_key] = sales_year.get(year_key,0)+item["total_sales"]
  sorted_d = sorted(sales_year.items(), key=operator.itemgetter(1), reverse=True)
  year_popular, sales_popular= sorted_d[0]
  #summary = [
  #  "The {} generated the most revenue: ${}".format(
  #    format_car(max_revenue["car"]), max_revenue["revenue"]),
  #]
  summary = [
    "The {} generated the most revenue: ${} \n The {} generated the most sales: {} \n The most popular year was {} "
    "with {} sales.".format( format_car(max_revenue["car"]), max_revenue["revenue"],
       format_car(max_sales["car"]), max_sales["total_sales"], year_popular,sales_popular),
  ]
  return summary


def cars_dict_to_table(car_data):
  """Turns the data in car_data into a list of lists."""
  table_data = [["ID", "Car", "Price", "Total Sales"]]
  for item in car_data:
    table_data.append([item["id"], format_car(item["car"]), item["price"], item["total_sales"]])
  return table_data


def main(argv):
  """Process the JSON data and generate a full report out of it."""
  data = load_data("/home/student-04-ac143191a1fb/car_sales.json")
  summary = process_data(data)
  print(summary)
  report_summary = summary[0].replace("\n","<br/>")
  # TODO: turn this into a PDF report
  table_data = cars_dict_to_table(data)
  reports.generate("/tmp/cars.pdf","Sales summary for last month",report_summary, table_data)
  # TODO: send the PDF report as an email attachment
  sender = "automation@example.com"
  receiver = "{}@example.com".format(os.environ.get('USER'))
  subject = "Sales summary for last month"


  message = emails.generate(sender, receiver, subject, summary[0],
                            "/tmp/cars.pdf")
  print(message)
  emails.send(message)


if __name__ == "__main__":
  main(sys.argv)