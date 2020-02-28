import re

print(re.search(r"[a-zA-Z]{5}","a ghost")) # find exactly 5 char word
print(re.search(r"[a-zA-Z]{5}","a ghost appeared")) # find exactly 5 char
# word, finds only first word
print(re.findall(r"[a-zA-Z]{5}","a scary ghost appeared")) # find exactly 5
# char
# word, finds all words
print(re.findall(r"\b[a-zA-Z]{5}","a scary ghost appeared")) # find exactly 5
# char
# word,
# find all full words
print(re.findall(r"\w{5,10}","I really like strawberries")) # find exactly 5
# -10 char word,
print(re.findall(r"\w{5,10}","I really like strawberries"))

print(re.findall(r"\w{5,}","I really like strawberries"))

print(re.search(r"s\w{,20}","I really like strawberries")) # starts with s
# followed by 20 alphanum chars

