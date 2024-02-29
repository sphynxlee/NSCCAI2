def has_pythagorean_triplet(num_list):
    # a**2 + b**2 == c**2
    square_list = [i**2 for i in num_list]
    for i in range(len(square_list)):
        for j in range(i+1, len(square_list)):
            if square_list[i] + square_list[j] in square_list:
                return True

    return False

test_list1 = [3, 1, 4, 6, 5]
print(has_pythagorean_triplet(test_list1))

test_list2 = [4, 6, 8, 15]
print(has_pythagorean_triplet(test_list2))