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



import string

def word_frequency_counter2 (text):
    output = {}

    print(f'string.punctuation: {string.punctuation}')
    punc_drop_translator = str.maketrans('', '', string.punctuation)
    print(f'punc_drop_translator: {punc_drop_translator}')
    clean_text = text.translate(punc_drop_translator)
    print(f'clean_text: {clean_text}')

    words = clean_text.split()
    print(f'words: {words}')

    for word in words:
        if word in output:
            output[word] += 1
        else:
            output[word] = 1

    return output

word_frequency_counter2("This is a practice problem. Practice makes perfect")

