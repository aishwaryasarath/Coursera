import re

#my_txt = "An investment in knowledge pays the best interest."
my_txt = "deegehgdfhfgjf"


def LetterCompiler(txt):
    result = re.findall(r'([a-c]).', txt)
    if result is None:
        return ""
    return result


print(LetterCompiler(my_txt))
