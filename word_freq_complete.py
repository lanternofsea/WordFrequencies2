
def word_freq_counter(sentence):
    """Counts the frequency of different words in a sentence and 
    returns a dictionary of word frequencies
    """
    # your code in this indented block below this line
    word_frequency = {}
   
   # search for a full stop at the right end of the string and remove if present
    sentence = sentence.rstrip(".")

    # split the sentence into list of words
    sentence_words = sentence.split(" ")

    for word in sentence_words:
        if word in word_frequency.keys( ):
            word_frequency[word] = word_frequency[word] + 1
        else:
            word_frequency[word] = 1

    return word_frequency



# Testing the function 

sentence1 = "Betty bought a bit of butter but the bit of butter was bitter so Betty bought a better bit of butter"
print(word_freq_counter(sentence1))

sentence2 = "She sells the sea shells on the sea shore."
print(word_freq_counter(sentence2))


