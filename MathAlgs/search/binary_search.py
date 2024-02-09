# binary search algorithm:
# 1. start with the middle item: if it's the target, you're done
# 2. if the target is less than the middle item, search the left half
# 3. if the target is greater than the middle item, search the right half
# 4. repeat until you find the target or the search space is empty

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