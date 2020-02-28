#!usr/bin/env python3

import shutil
import sys

def check_disk_usage(disk, min_absolute, min_percent):
    """Returns True if there is enough free space, false otherwise"""
    du = shutil.disk_usage(disk)

    #Calulate the percent of free space
    percent_free = du.free /du.total

    #Calculate how many free GBs
    gigabytes_free = du.free / 2**30

    if percent_free < min_percent or gigabytes_free < min_absolute:
        return False
    return True

#Check for atleast 2GB and 10% free
if not check_disk_usage("/",2,10):
    print("ERROR: Not enough disk space")
    sys.exit(1)

print("Everything ok")
sys.exit(0)



# cp disk_usage.py disk_usage_original.py
# cp disk_usage.py disk_usage_fixed.py

# diff -u disk_usage_original.py disk_usage_fixed.py > disk_usage.diff
