#When the starting point is greater than the stopping point, it forces the steps to be negative
#When, instead, the starting point is less than the stopping point, it forces the step to be positive
#Also, if the step is 0, it changes to 1 or -1. The result is returned as a one-line, space-separated string of numbers
def loop(start, stop, step):
	return_string = ""
	if step == 0:

	if start>stop:
		step = abs(step) * -1
	else:
		step = abs(step)
	for ___:
		return_string += str(count) + " "
	return return_string.strip()

print(loop(11,2,3)) # Should be 11 8 5  #steps to be negative, and until >stop
print(loop(1,5,0)) # Should be 1 2 3 4 #steps to be +1, until <stop
print(loop(-1,-2,0)) # Should be -1 #steps to be -1, until >stop
print(loop(10,25,-2)) # Should be 10 12 14 16 18 20 22 24, steps to be
# positive,
print(loop(1,1,1)) # Should be empty


# def counter(start, stop):
#     x = start
#     if start > stop:
#         return_string = "Counting down: "
#         while x >= stop:
#             return_string += str(x)
#             if x-2 != stop:
#                 return_string += ","
#             x-=1
#     else:
#         return_string = "Counting up: "
#         while x <= stop:
#             return_string += str(x)
#             if x-1!= stop:
#                 return_string += ","
#             x+=1
#     return return_string.rstrip(",")
#
# print(counter(1, 10)) # Should be "Counting up: 1,2,3,4,5,6,7,8,9,10"
# print(counter(2, 1)) # Should be "Counting down: 2,1"
# print(counter(5, 5)) # Should be "Counting up: 5"
