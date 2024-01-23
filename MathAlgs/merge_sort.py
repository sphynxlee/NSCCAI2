def merge_sort(arr):
    if len(arr) < 2:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] <= right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result.extend(left[left_index:])
    result.extend(right[right_index:])

    return result

# test:
arr = [38, 27, 43, 10]
sorted_arr = merge_sort(arr)
print("Original array:", arr)
print("Sorted array:", sorted_arr)

# time complexity: O(n log n)
# space complexity: O(n)