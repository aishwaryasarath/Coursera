# ratio = (1+5**(1/2))/2
# print(ratio)
#
# seconds_per_day = 86400
# days_per_week = 7
# seconds_per_week = seconds_per_day * days_per_week
# print("Seconds in a week: ", seconds_per_week)


# num_letters = 6
# possibilities_per_letter = 26
# num_possible_passwords = possibilities_per_letter ** num_letters
# print("Amount of possible passwords:", num_possible_passwords)

# disk_size = 16*1024*1024*1024
# sector_size = 512
# sector_amount = disk_size/sector_size
# print("number of sectors:", sector_amount)
#
#
# june_hours = 243
# june_cost = june_hours * 0.65
# print("In June we spent: " + str(june_cost))
#
# july_hours = 325
# july_cost = july_hours * 0.65
# print("In July we spent: " + str(july_cost))
#
# august_hours = 298
# august_cost = august_hours * 0.65
# print("In August we spent: " + str(august_cost))
#
# def print_monthly_expense(month, hours):
#     monthly_cost = hours * .65
#     print("In "+ month + " we spent: " + str(monthly_cost))
#
# june_hours = 243
# june_cost = print_monthly_expense("June", june_hours)
# july_hours = 325
# june_cost = print_monthly_expense("July", july_hours)
# august_hours = 298
# june_cost = print_monthly_expense("August", august_hours)

# def print_monthly_expense(month, hours):
#     montly_cost = hours * .65
#     print("In " + month + " we spent: " + str(monthly_cost))
# june_hours = 243
# june_cost = print_monthly_expense("June",june_hours)
# july_hours = 325
# july_cost = print_monthly_expense("July",july_hours)
# august_hours = 298
# august_cost = print_monthly_expense("August",august_hours)
# def convert_distance(miles):
#   km = miles * 1.6  # approximately 1.6 km in 1 mile
#   print("The distance in kilometers is " + str(km))
#   print("The round-trip in kilometers is " + str(km*2))
# convert_distance(55)
#
#
# def order_numbers(number1, number2):
# 	if number2 > number1:
# 		return number1, number2
# 	else:
# 		return number2, number1
#
# smaller,bigger = order_numbers(100, 99)
# print(smaller, bigger)

# number = 10
# if number > 11:
#   print(0)
# elif number != 10:
#   print(1)
# elif number >= 20 or number < 12:
#   print(2)
# else:
#   print(3)

# def calculate_storage(filesize):
#     block_size = 4096
#     # Use floor division to calculate how many blocks are fully occupied
#     full_blocks = (filesize // block_size)
#     print(full_blocks)
#     partial_block = filesize % block_size
#     print(partial_block)
#     if partial_block >= 1:
#         return block_size * (full_blocks + partial_block)
#     return block_size
#
# # print(calculate_storage(1))    # Should be 4096
# # print(calculate_storage(4096)) # Should be 4096
# # print(calculate_storage(4097)) # Should be 8192
# print(calculate_storage(8193))
# print("big" > "small")
# print(11 % 5)

#This function receives first_name and last_name, then prints a formatted string of "Name: last_name, first_name"
# if both names are not blank, or "Name: " with just one of the names, if the other one is blank, and nothing if both are blank.

# def format_name(first_name, last_name):
#     len_first= len(first_name)
#     len_last = len(last_name)
# 	if len_first >0 and len_last >0:
#         return
# 	return ""
#
# print(format_name("Ernest", "Hemingway"))
# # Should be "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should be "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should be "Name: Voltaire"
#
# print(format_name("", ""))
# # Should be ""

# def format_name(first_name, last_name):
#     len_first_name = len(first_name)
#     len_last_name = len(last_name)
#     if len_first_name > 0 and len_last_name > 0:
#         return "Name: " + last_name + "," + first_name
#     elif len_first_name > 0 and len_last_name == 0:
#         return "Name: " + first_name
#     elif len_first_name == 0 and len_last_name > 0:
#         return "Name: " + last_name
#     return ""
#
#
# print(format_name("Ernest", "Hemingway"))
# # Should be "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should be "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should be "Name: Voltaire"

# def format_name(first_name, last_name):
#   len_first_name = len(first_name)
#   len_last_name = len(last_name)
#   if len_first_name>0 and len_last_name>0:
#     return "Name: " + last_name +","+ first_name
#   elif len_first_name > 0 and len_last_name == 0:
# 	  return "Name: " + first_name
# 	elif len_first_name == 0 and len_last_name > 0:
# 	  return "Name: " + last_name
# 	return ""
#
# print(format_name("Ernest", "Hemingway"))
# # Should be "Name: Hemingway, Ernest"
#
# print(format_name("", "Madonna"))
# # Should be "Name: Madonna"
#
# print(format_name("Voltaire", ""))
# # Should be "Name: Voltaire"
#
# print(format_name("", ""))
# # Should be ""

# The fractional_part function divides the numerator by the denominator, and returns just the fractional part (a number between 0 and 1).
# Complete the body of the function so that it returns the right number.
# Note: Since division by 0 produces an error, if the denominator is 0, the function should return 0 instead of attempting the division.


# def fractional_part(numerator, denominator):
#     if numerator != 0 and denominator != 0:
#         result = (numerator / denominator) - (numerator // denominator)
#         return result
# # Operate with numerator and denominator to
# # keep just the fractional part of the quotient
#     return 0
#
# print(fractional_part(5, 5)) # Should be 0
# print(fractional_part(5, 4)) # Should be 0.25
# print(fractional_part(5, 3)) # Should be 0.66...
# print(fractional_part(5, 2)) # Should be 0.5
# print(fractional_part(5, 0)) # Should be 0
# print(fractional_part(0, 5)) # Should be 0

# print(((10 >= 5*2) and (10 <= 5*2)))
#
# def sum(x, y):
# 		return(x+y)
# print(sum(sum(1,2), sum(3,4)))
# print(11 % 5)
# print("big" > "small")

# def print_prime_factors(number):
#   # Start with two, which is the first prime
#   factor = 2
#   # Keep going until the factor is larger than the number
#   while factor <= number:
#     # Check if factor is a divisor of number
#     if number % factor == 0:
#       # If it is, print it and divide the original number
#       print(factor)
#       number = number / factor
#     else:
#       # If it's not, increment the factor by one
#       factor += 1
#   return "Done"
#
# print_prime_factors(100) # Should print 2,2,5,5
#
# def is_power_of_two(n):
# 	# Check if the number can be divided by two without a remainder
# 	if n == 0 or n == 1:
# 		return False
# 	while n % 2 == 0 and n != 0 and n>0:
# 		n = n / 2
# 	# If after dividing by two the number is 1, it's a power of two
# 	if n == 1:
# 		return True
# 	return False
# print(is_power_of_two(7))

#
#
# def sum_divisors(n):
# 	divisor = 2
# 	sum_divisor = 1
# 	while divisor < n and n!=0:
# 		if n % divisor == 0:
# 			sum_divisor += divisor
# 		divisor += 1
# 	if n != 0:
# 		return sum_divisor
# 	else:
# 		return 0
#
# print(sum_divisors(6))
# print(sum_divisors(12))
# print(sum_divisors(0))

# # sum of all the divisors of a number without including it
# divisor = 1
#
# if num % divisor

# def is_power_of_two(n):
#   # Check if the number can be divided by two without a remainder
#   if n == 1 or n < 0:
#     return False
#   while n % 2 == 0 and n != 0:
#     n = n / 2
#    # If after dividing by two the number is 1, it's a power of two
#   if n == 1:
#     return True
#   return False
#
# print(is_power_of_two(2))


# def is_power_of_two(n):
#   # Check if the number can be divided by two without a remainder
#   # if n == 1:
#   #   return False
#   while n %2 == 0 and n != 0:
#     n = n/2
#   if n == 1:
#     return True
#   return False
# print(is_power_of_two(1))
#
# def is_power_of_two(n):
# # Check if the number can be divided by two without a remainder
# # If after dividing by two the number is 1, it's a power of two

# def is_power_of_two(n):
#   # Check if the number can be divided by two without a remainder
#   if n <= 1:
#     return False
#   while n %2 == 0:
#     n = n/2
#   if n == 1:
#     return True
#   return False
#
# print(is_power_of_two(4))

# def square(n):
#   return n * n
#
#
# def sum_squares(x):
#   sum = 0
#   for n in range(x):
#     sum += square(n)
#   return sum
#
#
# print(sum_squares(10))  # Should be 285

# for left in range(7):
#   for right in range(left,7):
#     print("[" + str(left) + "|" + str(right) + "]", end=" ")
#   print()

#
# def validate_users(users):
#
#     for user in users:
#       if is_valid(user):
#         print(user + " is valid")
#       else:
#         print(user + " is invalid")


# def validate_users(users):
#   for user in users:
#     def is_valid(user):
#       if len(user) >= 3:
#         return True
#       else:
#         return False
#       if is_valid(user):
#         print(user + " is valid")
#       else:
#         print(user + " is invalid")
#
#
# validate_users(['taylor', 'luisa', 'jamaal'])
# validate_users(['purplecat'])

# def factorial(n):
#   result = 1
#   for x in range(1, n + 1):
#     result = result * x
#   return result
#
#
# for n in range(10):
#   print(n, factorial(n))

# for x in range(0,100,7):
#   print(x)

#
# def retry(operation, attempts):
#   for n in range(attempts):
#     if operation():
#       print("Attempt " + str(n) + " succeeded")
#       break
#     else:
#       print("Attempt " + str(n) + " failed")
#
# retry(create_user, 3)
# retry(stop_service, 5)

# number = 1
# while number <= 7:
# 	print(number, end=" ")
#     number +=1

# def show_letters(word):
# 	for letter in word:
# 		print(letter)
#
# show_letters("Hello")

# def digits(n):
#   count = 0
#   if n == 0:
#     ___
#   while (___):
#     count += 1
#     ___
#   return count
#
#
# print(digits(25))  # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000))  # Should print 4
# print(digits(0))  # Should print 1

# def digits(n):
#   count = 0
#   if n == 0:
#     count = 1
#   while (n/10) >0:
#     count += 1
#     n //= 10
#   return count
#
#
# print(digits(25))  # Should print 2
# print(digits(144))  # Should print 3
# print(digits(1000))  # Should print 4
# print(digits(0))  # Should print 1

# def multiplication_table(start, stop):
# 	for x in ___:
# 		for y in ___:
# 			print(str(x*y), end=" ")
# 		print()
#
# multiplication_table(1, 3)

# 1 2 3
#
# 2 4 6
#
# 3 6 9
# Should print the multiplication table shown above
# def multiplication_table(start, stop):
#   for x in range(start, stop+1):
#     print("x:" + str(x))
#     for y in range(start):
#       print(str(x*y), end=" ")
#     print()
#
# multiplication_table(1, 3)

# def multiplication_table(start, stop):
# 	for x in range(start, stop+1):
# 		for y in range(start, stop+1):
# 			print(str(x*y), end=" ")
# 		print()
#
# multiplication_table(1, 3)
#
# def votes(params):
# 	for vote in params:
# 	    print("Possible option:" + vote)
#
# # votes(['yes','no','maybe'])
#
for x in range(10):
    for y in range(x):
        print(y) #8
# print("--")
# for x in range(1, 10, 3):
#      print(x) #7

# def decade_counter():
# 	while year < 50:
# 		year += 10
# 	return year

# def loop(start, stop, step):
# 	return_string = ""
# 	if step == 0:
# 		___
# 	if ___:
# 		step = abs(step) * -1
# 	else:
# 		step = abs(step)
# 	for ___:
# 		return_string += str(count) + " "
# 	return return_string.strip()
#
# print(loop(11,2,3)) # Should be 11 8 5
# print(loop(1,5,0)) # Should be 1 2 3 4
# print(loop(-1,-2,0)) # Should be -1
# print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24
# print(loop(1,1,1)) # Should be empty

# def loop(start, stop, step):
# 	return_string = ""
# 	if step == 0:
# 		___
# 	if ___:
# 		step = abs(step) * -1
# 	else:
# 		step = abs(step)
# 	for ___:
# 		return_string += str(count) + " "
# 	return return_string.strip()
#
# print(loop(11,2,3)) # Should be 11 8 5
# print(loop(1,5,0)) # Should be 1 2 3 4
# print(loop(-1,-2,0)) # Should be -1
# print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24
# print(loop(1,1,1)) # Should be empty

# def first_and_last(message):
#   if (str(message[0]) != str(message[-1])):
#     return False
#   else:
#     return True
#
# print(first_and_last("else"))
# print(first_and_last("tree"))
# print(first_and_last(""))
#
#
# def is_palindrome(input_string):
#     new_string = ""
#     reverse_string = ""
#     for x in range(len(input_string)):
#         #print(input_string[x])
#         if not input_string[x].isspace():
#            # print(input_string[x].lower())
#             new_string += input_string[x].lower()
#             reverse_string = input_string[x].lower() + reverse_string
#     if reverse_string == new_string:
#         return True
#     return False
#     # print("new_string: "+new_string)
#     # print("reverse_string: "+reverse_string)
#
#
#
#
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True


# def is_palindrome(input_string):
# 	# We'll create two strings, to compare them
# 	new_string = ""
# 	reverse_string = ""
# 	# Traverse through each letter of the input string
# 	for ___:
# 		# Add any non-blank letters to the
# 		# end of one string, and to the front
# 		# of the other string.
# 		if ___:
# 			new_string = ___
# 			reverse_string = ___
# 	# Compare the strings
# 	if ___:
# 		return True
# 	return False
#
# print(is_palindrome("Never Odd or Even")) # Should be True
# print(is_palindrome("abc")) # Should be False
# print(is_palindrome("kayak")) # Should be True


# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km",
# with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
# def convert_distance(miles):
# 	km = miles * 1.6
# 	result = "{} miles equals {___} km".___
# 	return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km

# Using the format method, fill in the gaps in the convert_distance function so that it returns the phrase "X miles equals Y km",
# with Y having only 1 decimal place. For example, convert_distance(12) should return "12 miles equals 19.2 km".
# def convert_distance(miles):
# 	km = miles * 1.6
# 	result = "{} miles equals {:.1f} km".format(miles,km)
# 	return result
#
# print(convert_distance(12)) # Should be: 12 miles equals 19.2 km
# print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
# print(convert_distance(11)) # Should be: 11 miles equals 17.6 km
#

# def group_list(group, users):
#     members = ""
#     for user in users:
#         if members == "":
#             members = members + user
#         else:
#             members = members + ", " + user
#
#     #print(members)
#     return "{}: {}".format(group, members)
#
# print(group_list("Marketing", ["Mike", "Karen", "Jake", "Tasha"])) # Should be "Marketing: Mike, Karen, Jake, Tasha"
# print(group_list("Engineering", ["Kim", "Jay", "Tom"])) # Should be "Engineering: Kim, Jay, Tom"
# print(group_list("Users", "")) # Should be "Users:"
#
# def skip_elements(elements):
#     # code goes here
#     new_elements = []
#     for i in range(len(elements)):
#         if i%2 == 0:
#             new_elements.append(elements[i])
#     return new_elements
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
# print(skip_elements([])) # Should be []


# def skip_elements(elements):
# 	return [elem for index, elem in enumerate(elements) if index%2 == 0]
#
# print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
# print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']

# #-------begin
#
# filenames = ["program.c", "stdio.hpp", "sample.hpp", "a.out", "math.hpp","hpp.out"]
# newfilenames = []
# for filename in filenames:
#     if filename.endswith(".hpp"):
#         new =filename.replace(".hpp",".h")
#         newfilenames.append((new,filename))
#     else:
#         newfilenames.append((filename,filename))
# print(newfilenames)
#
# #----end

#print (newfilenames) # Should be [('program.c', 'program.c'), ('stdio.hpp',
# 'stdio.h'), ('sample.hpp', 'sample.h'), ('a.out', 'a.out'), ('math.hpp', 'math.h'), ('hpp.out', 'hpp.out')]
# def pig_latin(text):
#     say = ""
#     piglist = []
#
#     words = text.split()
#     for word in words:
#         pigword = word[1:]+word[0]+"ay"
#         piglist.append(pigword)
#     for pigw in piglist:
#         say = say+ pigw + " "
#     return say.rstrip()
#
#
# print(pig_latin("hello how are you"))  # Should be "ellohay owhay reaay ouyay"
# print(pig_latin(
#     "programming in python is fun"))  # Should be "rogrammingpay niay ythonpay siay unfay"
#
#
# def octal_to_string(octal):
#     result = ""
#     value_letters = [(4, "r"), (2, "w"), (1, "x")]
#     # Iterate over each of the digits in octal
#     for ___ in [int(n) for n in str(octal)]:
#         # Check for each of the permissions values
#         for value, letter in value_letters:
#             if ___ >= value:
#                 result += ___
#                 ___ -= value
#             else:
#                 ___
#     return result
#
#
# print(octal_to_string(755))  # Should be rwxr-xr-x
# print(octal_to_string(644))  # Should be rw-r--r--
# print(octal_to_string(750))  # Should be rwxr-x---
# print(octal_to_string(600))  # Should be rw-------

#
# wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
# for key, value in wardrobe.items():
#     #print(key,value)
#     for x in range(len(value)):
#         print("{} {}".format(value[x],key ))


# def groups_per_user(group_dictionary):
#     user_groups = {}
#     group_list =[]
#
#
#     for group, user in group_dictionary.items():
#
#         #print("group,user:",group, user)
#         for user_count in range(len(user)):
#             #print("user[user_count]:",user[user_count])
#             #print("user[user_count]:",user[user_count])
#             if group not in group_list:
#                 #print("appended", user_groups)
#                 group_list.append(group)
#                 user_groups[user[user_count]]=group_list
#                 #print("user_groups{}:",user_groups)
#             else:
#                 #print("--came to else:--",group, user_groups,user[user_count])
#                 newlist = []
#                 newlist.append(group)
#                 user_groups[user[user_count]] = newlist
#                 #print("user_groups{}:", user_groups,newlist)
#         #print("---------")
#     return (user_groups)
#
#
# print(groups_per_user({"local": ["admin", "userA"],"public": ["admin", "userB"],"administrator": ["admin"]}))
# # {"admin" : ["local","public", "administrator"], "userA" : ["local"],
# # "userB" : ["public"]}
#
#
# def format_address(address_string):
#     # Declare variables
#
#     # Separate the address string into parts
#
#     # Traverse through the address parts
#     for __:
#     # Determine if the address part is the
#     # house number or part of the street name
#
#     # Does anything else need to be done
#     # before returning the result?
#
#     # Return the formatted string
#     return "house number {} on street named {}".format(__)
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
