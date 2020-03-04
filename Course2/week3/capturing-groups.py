import re
result = re.search(r"^(\w*), (\w*)$", "Lovelace, Ada")
#print(result)
#
print(result.groups())
#print(result[0])
#print(result[1])
#print(result[2])
#
# print("{} {}".format(result[2], result[1]))

# def rearrange_name(name):
#     #result = re.search(r"^(\w*), (\w*)$", name)
#     result = re.search(r"^(\w*), (\w*) (\w*?.)$", name)
#     # also ^([\w \.-]*), ([\w \.-]*)$
#     print(result.groups())
#     if result is None:
#         return name
#     return print("{} {} {}".format(result[2], result[3], result[1]))
# #rearrange_name("Lovelace, Ada")
# rearrange_name("Kennedy, John F.")

# def rearrange_name(name):
#     #result = re.search(r"^(\w*), (\w*)$", name)
#     result = re.search(r"^([\w \.-]*), ([\w \.-]*)$", name)
#     # also
#     print(result.groups())
#     if result is None:
#         return name
#     return print("{} {}".format(result[2], result[1]))
# #rearrange_name("Lovelace, Ada")
# rearrange_name("Kennedy, John F.")
