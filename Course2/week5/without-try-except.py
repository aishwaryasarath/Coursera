def read_file(filename):
    if not os.path.exists(filename):
        return ""
    if not os.path.isfile(filename):
        return ""
    if not os.access(filename, os.R_OK):
        return ""
    if is_locked(filename):
        return ""
    if is_not_accessible(filename):
        return ""

