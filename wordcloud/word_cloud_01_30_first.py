def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and",
                           "or", "an", "as", "i", "me", "my", \
                           "we", "our", "ours", "you", "your", "yours", "he",
                           "she", "him", "his", "her", "hers", "its", "they",
                           "them", \
                           "their", "what", "which", "who", "whom", "this",
                           "that", "am", "are", "was", "were", "be", "been",
                           "being", \
                           "have", "has", "had", "do", "does", "did", "but",
                           "at", "by", "with", "from", "here", "when", "where",
                           "how", \
                           "all", "any", "both", "each", "few", "more", "some",
                           "such", "no", "nor", "too", "very", "can", "will",
                           "just", "in", \
                           "on", "not", "may", "thus", "one", "would", "two",
                           "us", "might", "also", "for", "these", "other",
                           "into", "those", \

                          "only", "other", "so", "than", "there", "same",
                           "between", "made", "even", "must", "most"]

    # LEARNER CODE START HERE

    # Dictionary to store frequencies of words
    word_dictionary = {}

    # splitting the contents of file to words
    list_words = file_contents.split()

    # looping through words to remove punctuations and add the word and its frequency to a dictionary
    for word in list_words:
        word = word.lower()
        for char in punctuations:
            word = word.replace(char, "")
        if word not in uninteresting_words:
            if word not in word_dictionary:
                word_dictionary[word] = 1
            else:
                word_dictionary[word] += 1

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(word_dictionary)
    return cloud.to_array()

# Display your wordcloud image

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()
