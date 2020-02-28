# file = open("romeo.txt")
# print(file.readline())
# print(file.read())
# file.close()
#
#
# with open("romeo.txt") as file:
#     for line in file:
#         print(line.strip().upper())
#
# file = open("romeo.txt")
# lines = file.readlines()
# file.close()
#
# lines.sort()
# print(lines)

# ## writing to files
# with open("to-write.txt","w") as file:
#     file.write("Once upon a time..")
# # old contents will be deleted if file already exists
# # "a" - append more, "r+" read-write mode, "r" - read mode "w" - write mode
#
#
# guests = open("guests.txt", "w")
# initial_guests = ["Bob", "Andrea", "Manuel", "Polly", "Khalid"]
#
# for i in initial_guests:
#     guests.write(i + "\n")
#
# guests.close()
#
# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)
#
# new_guests = ["Sam", "Danielle", "Jacob"]
#
# with open("guests.txt", "a") as guests:
#     for i in new_guests:
#         guests.write(i + "\n")
#
# guests.close()
#
# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)
#
# checked_out=["Andrea", "Manuel", "Khalid"]
# temp_list=[]
#
# with open("guests.txt", "r") as guests:
#     for g in guests:
#         temp_list.append(g.strip())
#
# with open("guests.txt", "w") as guests:
#     for name in temp_list:
#         if name not in checked_out:
#             guests.write(name + "\n")
#
# with open("guests.txt") as guests:
#     for line in guests:
#         print(line)
#
# guests_to_check = ['Bob', 'Andrea']
# checked_in = []
#
# with open("guests.txt","r") as guests:
#     for g in guests:
#         checked_in.append(g.strip())
#     for check in guests_to_check:
#         if check in checked_in:
#             print("{} is checked in".format(check))
#         else:
#             print("{} is not checked in".format(check))

import os
def create_python_script(filename):
  comments = "# Start of a new Python program"
  with open(filename, "w") as file:
    file.write(comments)
    file.close()
    filesize = os.path.getsize(filename)
    print(filesize)
  return(filesize)

print(create_python_script("program.py"))

# import os
#
#
# def new_directory(directory, filename):
#     # Before creating a new directory, check to see if it already exists
#     if not os.path.isdir(directory):
#         os.mkdir(directory)
#         os.chdir(directory)
#         # Create the new file inside of the new directory
#         file = open(filename, "w")
#         file.close()
#
#     # Return the list of files in the new directory
#
#         print(os.listdir(os.getcwd()))
#
# print(new_directory("PythonPrograms", "script.py"))
