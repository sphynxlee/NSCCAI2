def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            # Target found, return the index
            return i
    # Target not found in the list
    return -1

my_list = [1, 3, 5, 7, 9, 11, 13]
target_value = 7
result = linear_search(my_list, target_value)

if result != -1:
    print(f"Target {target_value} found at index {result}.")
else:
    print(f"Target {target_value} not found in the list.")
