def word_frequency_counter(text):
    word_list = text.split()
    word_freq = {}
    for word in word_list:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    return word_freq

text = "This is a practice problem. Practice makes perfect"

result = word_frequency_counter(text)
print(result)