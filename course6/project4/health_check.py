#!/usr/bin/env python3
import requests
import os
import socket
import shutil
import psutil
import sys
import emails


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    return usage < 80


def check_disk_usage(disk, min_absolute):
    """Returns True if there is enough free space, false otherwise"""
    du = shutil.disk_usage(disk)

    #Calculate how many free bytes
    bytes_free = du.free

    if bytes_free < min_absolute:
        return False
    return True

def check_disk_usage_perc(disk, min_percent):
    """Returns True if there is enough free space, false otherwise"""
    du = shutil.disk_usage(disk)

    #Calulate the percent of free space
    percent_free = du.free /du.total * 100

    if percent_free < min_percent:
        return False
    return True

def check_localhost():
        localhost = socket.gethostbyname('localhost')
        return localhost=="127.0.0.1"

def main():
    subject = "Error - "
    send_flag = False
    if  not check_cpu_usage():
        subject += "CPU usage is over 80%"
        send_flag = True
    elif not check_localhost():
         subject += "localhost cannot be resolved to 127.0.0.1"
         send_flag = True
    elif not check_disk_usage_perc("/",20):
        subject += "Available disk space is less than 20%"
        send_flag = True
    elif not check_disk_usage("/",500*2**20):
        subject += "Available memory is less than 500 MB"
        send_flag = True

    if send_flag:
        body = "Please check your system and resolve the issue as soon as possible"
        sender = "automation@example.com"
        receiver = "{}@example.com".format(os.environ.get('USER'))
        message = emails.generate_error_report(sender, receiver, subject, body)
        #print(message)
        emails.send(message)

if __name__ == "__main__":
  main()



