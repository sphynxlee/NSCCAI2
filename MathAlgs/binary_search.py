def binary_search (list, target):
    left = 0
    right = len(list) - 1
    while left <= right:
        midpoint = (left + right) // 2
        current_item = list[midpoint]
        if current_item == target:
            return midpoint
        elif target < current_item:
            right = midpoint - 1
        else:
            left = midpoint + 1
    return -1

my_list = [2, 3, 4, 5, 6, 7, 9, 11, 13]
target_value = 7
result = binary_search(my_list, target_value)
print(result)

# time complexity: O(log n)
# space complexity: O(1)