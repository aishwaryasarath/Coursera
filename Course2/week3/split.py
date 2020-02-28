import re
print(re.split(r"[.?!]","One sentence. Another one? Yet another one!")) # to
# split
print(re.split(r"([.?!])","One sentence. Another one? Yet another one!")) #
# to split and to have the elements that we use to split

print(re.sub(r"[\w.%+-]+@[\w.-]+","[REDACTED]","Received an email for "
                                               "go_pro95@my.example.com"))
print(re.sub(r"^([\w .-]*), ([\w .-]*)$", r"\2 \1", "Lovelace, Ada"))
