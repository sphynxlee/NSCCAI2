# Write a function that creates a size n integer list with single, random number missing.
# The function should scramble the order of the integers in the list, then return the list and the missing number as a tuple

import random

def generate_list_with_missing_number(n):
    # Create a list of integers from 1 to n
    number_list = list(range(1, n + 1))

    # Choose a random index to remove an element
    missing_index = random.randint(0, n - 1)

    # Remove the element at the chosen index to create a missing number
    missing_number = number_list.pop(missing_index)

    # Shuffle the remaining elements in the list
    random.shuffle(number_list)

    # Return a tuple containing the shuffled list and the missing number
    return number_list, missing_number

n = 10
result = generate_list_with_missing_number(n)
print("Shuffled List:", result[0])
print("Missing Number:", result[1])

# Write a function that takes the scrambled list and returns the missing number.
# It should use mergesort or quicksort and a linear search.
# No, I’m not looking for the fastest solution  I’m looking for you to practice writing mergesort or quicksort from memory.