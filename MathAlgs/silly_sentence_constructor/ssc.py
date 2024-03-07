import random
import os

def sentence_translator(sentence, data_path):
    # Read the raw data from the file
    word_lists = {}

    with open(data_path, 'r') as f:
        for line in f:
            row = line.strip().split(',')
            letter = row[0]
            words = row[1:]
            word_lists[letter.upper()] = words

    # Function to replace each word with a randomly chosen word from the corresponding list
    def replace_word(word):
        first_letter = word[0].upper()
        word_list = word_lists.get(first_letter, [word])
        return random.choice(word_list)

    # Apply the replacement to each word in the sentence
    modified_sentence = ' '.join(replace_word(word) for word in sentence.split())
    return modified_sentence

# Example usage
data_path = os.getcwd() + '/NSCCAI2/MathAlgs/silly_sentence_constructor/challenge.txt'
input_sentence = "Python is amazing"
output_sentence = sentence_translator(input_sentence, data_path)
print(output_sentence)
