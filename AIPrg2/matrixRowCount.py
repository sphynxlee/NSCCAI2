# Given a 2D matrix where each individual row is sorted in ascending
# order, write a function named row_count that takes two parameters -
# the matrix (matrix) and a target value (target). The function should
# return the number of rows in which the target value is present

def target_finder(matrix, target):
    for index, value in enumerate(matrix):
        if target in value:
            return index
    return -1

matrix = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]

target_value = 20
result = target_finder(matrix, target_value)
print(f"index of rows containing {target_value}: {result}")


def row_count(matrix, target):
    count = 0
    for row in matrix:
        if target in row:
            count += 1
    return count

matrix = [
    [1, 3, 5, 7],
    [2, 4, 6, 8],
    [0, 9, 10, 11]
]

target_value = 6
result = row_count(matrix, target_value)
print(f"Number of rows containing {target_value}: {result}")
