import re
# def transform_record(record):
#
#
#   new_record = re.sub(r"([0-9]{3})-([0-9]{3})-?([0-9]{4})\b", r"+1-\1-\2-\3",
#                       record)
#   return new_record

def transform_record(record):

    if re.search(r"([0-9]{3})-([0-9]{7})",record):

        new_record = re.sub(r"([0-9]{3})-([0-9]{3})-?([0-9]{4})\b", r"+1-\1-\2\3",
                      record)
    elif re.search(r"([0-9]{3})-([0-9]{3})-?([0-9]{4})\b", record):
        new_record = re.sub(r"([0-9]{3})-([0-9]{3})-?([0-9]{4})\b",
                            r"+1-\1-\2-\3",
                            record)
    return new_record


print(transform_record("Sabrina Green,802-867-5309,System Administrator"))
# Sabrina Green,+1-802-867-5309,System Administrator

print(transform_record("Eli Jones,684-3481127,IT specialist"))
# Eli Jones,+1-684-3481127,IT specialist

print(transform_record("Melody Daniels,846-687-7436,Programmer"))
# Melody Daniels,+1-846-687-7436,Programmer

print(transform_record("Charlie Rivera,698-746-3357,Web Developer"))
# Charlie Rivera,+1-698-746-3357,Web Developer


# ([0-9]{3})-([0-9]{7})
