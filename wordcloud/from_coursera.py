import wordcloud
import numpy as np
from matplotlib import pyplot as plt
#from IPython.display import display
#import fileupload
import io
import sys



def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and",
                           "or", "an", "as", "i", "me", "my",
                           "we", "our", "ours", "you", "your", "yours", "he",
                           "she", "him", "his", "her", "hers", "its", "they",
                           "them",
                           "their", "what", "which", "who", "whom", "this",
                           "that", "am", "are", "was", "were", "be", "been",
                           "being",
                           "have", "has", "had", "do", "does", "did", "but",
                           "at", "by", "with", "from", "here", "when", "where",
                           "how",
                           "all", "any", "both", "each", "few", "more", "some",
                           "such", "no", "nor", "too", "very", "can", "will",
                           "just"]

    # LEARNER CODE START HERE
    input_file = open('newphysics.txt', mode='r', encoding='utf-8-sig')

    file_contents = {}
    for line in input_file:
        line = line.rstrip()
        line = line.lower()
        for char in line:
            if char in punctuations:
                line = line.replace(char, "")
        words = line.split()
        for word in words:
            if word not in stop_words:
                if word not in file_contents:
                    file_contents[word] = 1
                else:
                    file_contents[word] += 1

    print(file_contents)

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(file_contents)
    return cloud.to_array()


# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
