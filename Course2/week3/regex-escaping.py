import re
# print(re.search(r".com","welcome"))
# print(re.search(r"\.com","welcome")) # check for . by escaping it
# # \n new line \t tab
# # \w any alphanum chars, \s for space, \b forword boundaries
# print(re.search("\w*","This is an example"))
# print(re.search("\w*","And_this_is_another"))

#at least 2 groups of alphanumeric characters (including letters, numbers
# and underscores) separated by one or more whitespace characters.

def check_character_groups(text):
  result = re.search(r"\w\w* (w*)?", text)
  return result != None

print(check_character_groups("One")) # False
print(check_character_groups("123  Ready Set GO")) # True
print(check_character_groups("username user_01")) # True
print(check_character_groups("shopping_list: milk, bread, eggs.")) # False
