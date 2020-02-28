#!/usr/bin/env python3
import sys
import os
import re


def error_search(log_file):
    error = input("What is the error? ")
    returned_errors = []
    with open(log_file, mode='r', encoding='UTF-8') as file:
        for log in file.readlines():
            error_patterns = ["error"]
            for i in range(len(error.split(' '))):
                error_patterns.append(
                    r"{}".format(error.split(' ')[i].lower()))
            if all(re.search(error_pattern, log.lower()) for error_pattern in
                   error_patterns):
                returned_errors.append(log)
        file.close()
    return returned_errors


def file_output(returned_errors):
    #with open(os.path.expanduser('~') + '/data/errors_found.log','w') as file:
    with open(os.path.expanduser('~') + '/PycharmProjects/PythonED/CourseraGoogle/Course2/week4/errors_found.log', 'w') as file:
        for error in returned_errors:
            file.write(error)
        file.close()


if __name__ == "__main__":
    log_file = sys.argv[1]
    returned_errors = error_search(log_file)
    file_output(returned_errors)
    sys.exit(0)

# o/p -> July 31 04:11:32 mycomputername CRON[51253]: ERROR: Failed to start CRON job due to script syntax error. Inform the CRON job owner!
