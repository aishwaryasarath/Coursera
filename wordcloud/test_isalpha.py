
input_file = open('romeo-full.txt', mode='r', encoding='utf-8-sig')

word_dictionary = {}
for line in input_file:
    line = line.rstrip()
    line_without_punctuation = ""
    for char in line:
        if char.isalpha() == True and char.isspace()== False:
            line_without_punctuation += char
    line = line_without_punctuation

    line = line.lower()
    words = line.split()
    for word in words:
        # if word not in stop_words:
        if word not in word_dictionary:
            word_dictionary[word] = 1
        else:
            word_dictionary[word] += 1


print(word_dictionary)


