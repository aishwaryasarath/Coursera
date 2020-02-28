import re
print(re.search(r"Py.*n","Pygmalion")) #.* any number of characters
print(re.search(r"Py.*n","Python programming")) #greedy
print(re.search(r"Py[a-z]*n","Python programming"))
print(re.search(r"Py[a-z]*n","Pyn")) #zero times is also a possibility


# + one or more chars that comes before it
print(re.search(r"o+l+","goldfish"))
print(re.search(r"o+l+","woolly"))
print(re.search(r"o+l+","boil"))
