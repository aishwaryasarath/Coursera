
#!/usr/bin/env python3
#from __future__ import print_function
import subprocess
import os
import multiprocessing
from multiprocessing import Pool

src = "/home/student-00-f0cade6c347a/data/prod/"
dest = "/home/student-00-f0cade6c347a/data/prod_backup/"
src_sub_dir_list = []
#print(os.getcwd())
def file_walk():
        for dir_path, subdir_list, file_list in os.walk(src):
                for subdir in subdir_list:
                        full_path = os.path.join(dir_path, subdir)
                        #print(full_path)
                        src_sub_dir_list.append(full_path)
        #print(src_sub_dir_list)
        return src_sub_dir_list

def run(src):
        subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
        cpu_count = multiprocessing.cpu_count()
        p = Pool(cpu_count)
        sub_dir_list = file_walk()
        p.map(run, sub_dir_list)


