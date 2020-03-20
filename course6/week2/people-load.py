import json

# The load() method does the inverse of the dump() method. It deserializes JSON from a file into basic Python objects.
# The loads() method also deserializes JSON into basic Python objects, but parses a string instead of a file.

with open('people.json', 'r') as people_json:
    people = json.load(people_json)
print(people)
