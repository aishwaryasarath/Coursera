#The uploader widget saved the contents of your uploaded file into a string
# object named file_contents that your word cloud script can process.

#Write a function in the cell below that iterates through the words in
# file_contents, removes punctuation, and counts the frequency of each word. Oh,
# and be sure to make it ignore word case, words that do not contain all alphabets
# and boring words like "and" or "the". Then use it in the generate_from_frequencies function to generate your very own word cloud!

#Hint: Try storing the results of your iteration in a dictionary before
# passing them into wordcloud via the generate_from_frequencies function.
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

    # wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies()
    return cloud.to_array()

# Display your wordcloud image

myimage = calculate_frequencies(file_contents) # string object from uploader
# widget
plt.imshow(myimage, interpolation = 'nearest')
plt.axis('off')
plt.show()

#If your word cloud image did not appear, go back and rework your calculate_frequencies function until you get
# the desired output. Definitely check that you passed your frequecy count dictionary into the generate_from_
# frequencies function of wordcloud. Once you have correctly displayed your word cloud image, you are all done with this project. Nice work!
