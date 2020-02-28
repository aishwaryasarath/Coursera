# import re
# # print(re.search(r"A.*a","Argentina"))
# # print(re.search(r"A.*a","Azerbijan"))
# # print(re.search(r"^A.*a$","Azerbijan"))
# # print(re.search(r"^A.*a$","Australia"))
#
# #valid variable name in python check
# pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
# print(re.search(pattern,"_this_is_a_valid_variable_name"))
# print(re.search(pattern,"my_variable1"))
# print(re.search(pattern,"2_myvar"))


#We said it needs to start with a letter. So we'll start with circumflex to indicate that we wanted to start from the beginning, and now a character class with all lowercase and uppercase letters plus the underscore.
#The rest of the variable can have as many numbers letters or underscores that we want. So we needed another character class this time containing numbers with a star at the end.
#Okay, we're almost done. You definitely deserve a star at the end of this. One last thing, we want this to be the end of the string that we're matching. Otherwise, we could match something that could be a variable, but that also contains additional stuff after it. So we finish up with a dollar sign.

#it starts with an uppercase letter, followed by at least some lowercase letters or a space, and ends with a period, question mark, or exclamation point.

import re
def check_sentence(text):
  result = re.search(r"^[A-Z]", text)
  return result != None

print(check_sentence("Is this is a sentence?")) # True
print(check_sentence("is this is a sentence?")) # False
print(check_sentence("Hello")) # False
print(check_sentence("1-2-3-GO!")) # False
print(check_sentence("A star is born.")) # True
