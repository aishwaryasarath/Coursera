import re
result = re.search(r"aza", "plaza") # r means it should process as raw string
print(result)
result = re.search(r"aza", "bazaar")
print(result)
result = re.search(r"aza", "maze")
print(result) # returns none, ie didnt find a match
print(re.search(r"^x","xenon"))
print(re.search(r"p.ng","penguin"))
print(re.search(r"p.ng","clapping"))
print(re.search(r"p.ng","pong"))
print(re.search(r"p.ng","Pangaea", re.IGNORECASE)) # to ignore case

def check_aei (text):
  result = re.search(r"a.e.i", text)
  return result != None

print(check_aei("academia")) # True
print(check_aei("aerial")) # False
print(check_aei("paramedic")) # True

