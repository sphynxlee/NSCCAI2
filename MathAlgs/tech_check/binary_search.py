def binary_search (list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        midpoint = (left + right) // 2
        current_element = list[midpoint]
        if current_element == target:
            return midpoint
        elif target < current_element:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]


target1 = 14
result1 = binary_search(my_list, target1)
print(f'The index of {target1} is {result1}')

target2 = 22
result2 = binary_search(my_list, target2)
print(f'The index of {target2} is {result2}')

# time complexity: O(log n)
# space complexity: O(1)