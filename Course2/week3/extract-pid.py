import re

log = "July 31 07:51:48 mycomputer bad_process[12345]: ERROR Performing " \
      "package update"

def extract_pid(log_line):
    regex = r"\[(\d+)\]"
    result = re.search(regex,log_line)
    if result is None:
        return ""
    return result[1]

print(extract_pid(log))
print(extract_pid("99 eleph in a [cage]"))
