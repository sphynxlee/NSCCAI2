matrix = [
    [1,2,3],
    [0, -1, -2],
    [4,5,6],
]

def detect_positive_negative_value (matrix):
    positive_counter = 0
    negative_counter = 0

    for row in matrix:
        for ele in row:
            if ele < 0:
                negative_counter += 1
            else:
                positive_counter += 1

    return (positive_counter, negative_counter)

print(detect_positive_negative_value(matrix))