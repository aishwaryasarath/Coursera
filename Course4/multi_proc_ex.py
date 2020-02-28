from multiprocessing import pool


def run(src, dest):
    subprocess.call(["rsync", "-arq", src, dest])


def file_walk():
    file_list, path_list = [], []
    init = os.getcwd()

    for root, dirs, files in os.walk('.'):
        dirs.sort()
        for file in files:
            file_list.append(file)
            os.chdir(root)
            path_list.append(os.getcwd())
            os.chdir(init)

        return file_list, path_list


def pool_handler():
    tasks = ['task1', 'task2', 'task3']
    cpu_count = multiprocessing.cpu_count()
    p = Pool(cpu_count)
    files, paths = file_walk()
    pathfile = [[paths[i], files[i]] for i in range(len(files))]
    p.map(run, tasks)


if __name__ == '__main__':
    pool_handler()

