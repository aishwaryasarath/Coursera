#!/usr/bin/env python3

import re

def rearrange_name(name):
    result = re.search(r"^([\w .]*), ([\w .]*)$", name)
    if result is None:
        # when blank names are given
        #return ""
        return name # to fix when only one name is given
    return "{} {}".format(result[2], result[1])



# Type in terminal
#------------------
# python3
# from rearrange import rearrange_name
# >>> rearrange_name("Lovelace, Ada")
