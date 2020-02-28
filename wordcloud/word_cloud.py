"""Create a dictionary with words and word frequencies that can be passed to
the generate_from_frequencies function of the WordCloud class."""

from wordcloud import wordcloud, STOPWORDS
import string
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
new_stop_words = ['may', 'thus', 'one', 'would', 'two', 'us', 'might', 'also']
for len in range(len(new_stop_words)):
    stop_words.add(new_stop_words[len])


# Before processing any text, you need to remove all the punctuation marks.
# To do this, you can go through each line of text, character-by-character,
# using the isalpha() method. This will check whether or not the character
# is a letter.
# To split a line of text into words, you can use the split() method.
# Before storing words in the frequency dictionary, check if they’re part of
# the "uninteresting" set of words (for example: "a", "the", "to", "if").
# Make this set a parameter to your function so that you can change it if
# necessary.


#Input file
# For the input file, you need to provide a file that contains text only.
# For the text itself, you can copy and paste the contents of a website you like.
# Or you can use a site like Project Gutenberg to find books that are available
# online. You could see what word clouds you can get from famous books,
# like a Shakespeare play or a novel by Jane Austen.


input_file = open('newphysics.txt', mode='r', encoding='utf-8-sig')

counts = dict()
for line in input_file:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in stop_words:
            if word not in counts:
                counts[word] = 1
            else:
                counts[word] += 1


print(counts)


#Once you have the dictionary, use this code to generate the word cloud image:
cloud = wordcloud.WordCloud(width=1280, height=720)

#cloud = wordcloud.WordCloud()
cloud.generate_from_frequencies(counts)
cloud.to_file("WordCloud.jpg")



