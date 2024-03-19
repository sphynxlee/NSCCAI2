# Triangle numbers: T_n = n(n+1)/2
# Pentagonal numbers: P_n = n(3n-1)/2
# Hexagonal numbers: H_n = n(2n-1)

# Problem: Find the smallest number that is simultaneously a triangular
# number, a pentagonal number, and a hexagonal number, and greater than a
# given limit.
# The sequence of triangle numbers is 1, 3, 6, 10, 15, and so on. The sequence
# of pentagonal numbers is 1, 5, 12, 22, 35, and so on. The sequence of
# hexagonal numbers is 1, 6, 15, 28, 45, and so on.
# Write a function find_common_numbers(limit) that calculates and returns
# the first number that is simultaneously a triangular number, a pentagonal
# number, and a hexagonal number, and greater than the given limit.


# def find_common_numbers(limit):
#     n = 1
#     while True:
#         triangle = n * (n + 1) // 2
#         pentagon = n * (3 * n - 1) // 2
#         hexagon = n * (2 * n - 1)
#         if triangle > limit and triangle == pentagon and triangle == hexagon:
#             return triangle
#         n += 1

# print(find_common_numbers(1))

def find_common_numbers(limit):
    # Function to check if a number is triangular
    def is_triangular(num):
        n = int((2 * num) ** 0.5)
        return n * (n + 1) // 2 == num

    # Function to check if a number is pentagonal
    def is_pentagonal(num):
        n = int((24 * num + 1) ** 0.5 + 1) // 6
        return n * (3 * n - 1) // 2 == num

    # Function to check if a number is hexagonal
    def is_hexagonal(num):
        n = int((2 * num) ** 0.5 + 1) // 4
        return n * (2 * n - 1) == num

    # Start iterating from the limit
    n = limit + 1
    while True:
        if is_triangular(n) and is_pentagonal(n) and is_hexagonal(n):
            return n
        n += 1

# Example usage:
limit = 1
result = find_common_numbers(limit)
print("The smallest number that is simultaneously a triangular, pentagonal, and hexagonal number, and greater than", limit, "is:", result)
