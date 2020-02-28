import os
import subprocess
from multiprocessing import Pool
import multiprocessing

src = "prod/"
dest = "prod_backup/"
#print(os.getcwd())
src_sub_dir_list = []


def file_walk():

    for dir_path, subdir_list, file_list in os.walk(src):
        for subdir in subdir_list:
            full_path = os.path.join(dir_path, subdir)
            src_sub_dir_list.append(full_path)
    return src_sub_dir_list


def run(src):

    subprocess.call(["rsync", "-arq", src, dest])

if __name__ == "__main__":
    cpu_count = multiprocessing.cpu_count()
    p = Pool(cpu_count)
    sub_dir_list = file_walk()
    p.map(run, sub_dir_list)


