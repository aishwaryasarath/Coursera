# def format_address(address_string):
#     # Declare variables
#     housenumber =""
#     streetname = ""
#     new_string = []
#     # Separate the address string into parts
#     new_string = address_string.split()
#     # Traverse through the address parts
#     #print(address_string.split()
#     for count,word in enumerate(new_string):
#     # Determine if the address part is the
#     # house number or part of the street name
#         if count == 0:
#             housenumber+= word
#         else:
#             streetname += word + " "
#
#     streetname.lstrip()
#     # Does anything else need to be done
#     # before returning the result?
#
#     # Return the formatted string
#     return "house number {} on street named {}".format(housenumber,streetname)
#
#
# print(format_address("123 Main Street"))
# # Should print: "house number 123 on street named Main Street"
#
# print(format_address("1001 1st Ave"))
# # Should print: "house number 1001 on street named 1st Ave"
#
# print(format_address("55 North Center Drive"))
# # Should print "house number 55 on street named North Center Drive"


# def highlight_word(sentence, word):
# 	return(sentence.replace(word, word.upper()))
#
# print(highlight_word("Have a nice day", "nice"))
# print(highlight_word("Shhh, don't be so loud!", "loud"))
# print(highlight_word("Automating with Python is fun", "fun"))


# def combine_lists(list1, list2):
#   list1.reverse()
#   list2.extend(list1)
#   return list2
# Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"] # did next, but in reverse
# Drews_list = ["Mike", "Carol", "Greg", "Marcia"] #did first
#
# print(combine_lists(Jamies_list, Drews_list))


# def count_letters(text):
#   result = {}
#   # Go through each letter in the text
#   for letter in text:
#     # Check if the letter needs to be counted or not
#     if letter.isalpha():
#         #letter.lower()
#         result[letter.lower()] = result.get(letter.lower(),0) + 1
#     # Add or increment the value in the dictionary
#
#   return result
#
# print(count_letters("AaBbCc"))
# # Should be {'a': 2, 'b': 2, 'c': 2}
#
# print(count_letters("Math is fun! 2+2=4"))
# # Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}
#
# print(count_letters("This is a sentence."))
# # Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}


# def combine_guests(guests1, guests2):
#   # Combine both dictionaries into one, with each key listed
#   # only once, and the value from guests1 taking precedence
#   guests2.update(guests1)
#   return guests2
#
# Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
# Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}
#
# print(combine_guests(Rorys_guests, Taylors_guests))
# class Person:
#     def __init__(self, name):
#         self.name = name
#
#     def greeting(self):
#         # Should return "hi, my name is " followed by the name set.
#         return "hi, my name is {}".format(self.name)
#
# # Create a new instance with a name of your choice
# some_person = Person("Aish")
# # Call the greeting method
# print(some_person.greeting())
#
#
# class ClassName:
#     """Documentation for the class."""
#
#     def method_name(self, other_parameters):
#         """Documentation for the method."""
#         body_of_method
#
#
# def function_name(parameters):
#     """Documentation for the function."""
#     body_of_function
#

class Elevator:
    def __init__(self, bottom, top, current):
        """Initializes the Elevator instance."""
        self.bottom = bottom
        self.top = top
        self.current = current

    def __str__(self):
        return "Current floor:{}".format(self.current)

    def up(self):
        """Makes the elevator go up one floor."""
        self.current += 1
        if self.current > self.top:
            self.current = self.top
        return self.current

    def down(self):
        """Makes the elevator go down one floor."""
        self.current -= 1
        if self.current < self.bottom:
            self.current = self.bottom
        return self.current

    def go_to(self, floor):
        """Makes the elevator go to the specific floor."""
        self.current = floor
        return self.current


elevator = Elevator(-1, 10, 0)
print(elevator)
elevator.up()
print(elevator.current)
