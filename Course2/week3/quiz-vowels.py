import re
def multi_vowel_words(text):
    list_words = re.split("\s",text)
    final_words= []
    for word in list_words:
        pattern = r"[aeiou]{3}"
        if re.findall(pattern, word):
            final_words.append(word)
    return final_words

print(multi_vowel_words("Life is beautiful"))
# ['beautiful']

print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# ['Obviously', 'queen', 'courageous', 'gracious']

print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# ['rambunctious', 'quietly', 'delicious']

print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# ['queue']

print(multi_vowel_words("Hello world!"))
# []

# import re
# def multi_vowel_words(text):
#   pattern = r"([aeiou]{3})
#   result = re.findall(pattern, text)
#   return result
#
# print(multi_vowel_words("Life is beautiful"))
# # ['beautiful']
#
# print(multi_vowel_words("Obviously, the queen is courageous and gracious."))
# # ['Obviously', 'queen', 'courageous', 'gracious']
#
# print(multi_vowel_words("The rambunctious children had to sit quietly and await their delicious dinner."))
# # ['rambunctious', 'quietly', 'delicious']
#
# print(multi_vowel_words("The order of a data queue is First In First Out (FIFO)"))
# # ['queue']
#
# print(multi_vowel_words("Hello world!"))
# # []
