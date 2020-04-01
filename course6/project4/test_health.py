import shutil
import psutil
#import network
import sys


def check_cpu_usage():
    usage = psutil.cpu_percent(1)
    print("cpu usage: ", usage)
    return usage < 80

if  not check_cpu_usage():
    print("ERROR!")

du = shutil.disk_usage("/")
print("free: ", du.free)
percent_free = du.free /du.total * 100
print("percent_free: ",percent_free)

megabytes_free = du.free / 2**20
print(megabytes_free)
print(megabytes_free>500)
print(du.free > 500*2**20)

# if check_localhost() and check_connectivity():
#     print("Everything ok")

