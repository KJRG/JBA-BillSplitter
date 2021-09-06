# put your python code here
text = input()
word_frequencies = dict()
for single_word in text.split():
    word_lowercase = single_word.lower()
    occurrences = word_frequencies.get(word_lowercase, 0)
    word_frequencies[word_lowercase] = occurrences + 1
for word, frequency in word_frequencies.items():
    print(word, frequency)
