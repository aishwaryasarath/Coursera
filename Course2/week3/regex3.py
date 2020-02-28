# character classes written in []
import re
print(re.search(r"[Pp]ython","Python"))
print(re.search(r"[a-z]way","What a way to go"))
print(re.search(r"cloud[a-zA-Z0-9]","cloudy"))
print(re.search(r"cloud[a-zA-Z0-9]","cloud9"))
print(re.search(r"[^a-zA-Z]","This is a sentence with spaces.")) # ^ to get
# chars that dont match

print(re.search(r"[^a-zA-Z ]","This is a sentence with spaces.")) #to search
# for not chars and not spaces
# returns the . at the end of the sentence
print(re.search(r"cat|dog","I like cats.")) # cat or dog
print(re.search(r"cat|dog","I like dogs.")) # cat or dog
print(re.search(r"cat|dog","I like cats and dogs.")) # cat or dog # two
# matches but we get only the first one
#if we need to find all matches, we need to use findall

print(re.findall(r"cat|dog","I like cats and dogs.")) # cat or dog
