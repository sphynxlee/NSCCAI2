# Given a list of words and a query word, write a function to
# determine if the query word is a concatenation of two words in the
# list. Brute force is not an acceptable solution. Can you think of a
# clever approach?

# Examples:
# print(cat_query(["cat", "dog", "bird", "cats", "doggy"], "catsdogs")) # => False
# print(cat_query(["cat", "dog", "bird", "cats", "doggy"], "birddog")) #=> True

def cat_query(words, query):
    word_set = set(words)
    n = len(query)

    def is_prefix_plus(word):
        return query.startswith(word) and query[len(word):] in word_set

    def is_suffix_plus(word):
        return query.endswith(word) and query[:-len(word)] in word_set

    for word in words:
        if is_prefix_plus(word) or is_suffix_plus(word):
            return True

    return False

print(cat_query(["cat", "dog", "bird", "cats", "doggy"], "birddog"))
