"""Create a dictionary with words and word frequencies that can be passed to
the generate_from_frequencies function of the WordCloud class."""

from wordcloud import wordcloud
import string
import nltk
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
uninteresting_words = ['may', 'thus', 'one', 'would', 'two', 'us', 'might',
                    'also']
for len in range(len(new_stop_words)):
    stop_words.add(uninteresting_words[len])


input_file = open('newphysics.txt', mode='r', encoding='utf-8-sig')

word_dictionary = {}
for line in input_file:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in stop_words:
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1


print(word_dictionary)


#Once you have the dictionary, use this code to generate the word cloud image:
cloud = wordcloud.WordCloud(width=1280, height=720)
cloud.generate_from_frequencies(word_dictionary)
cloud.to_file("WordCloud.jpg")



