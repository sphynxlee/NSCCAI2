# insertion sort algorithm:
# 1. start with the first item: it's already sorted
# 2. move to the next item
# 3. insert it into the correct position in the sorted list
# 4. repeat until the list is sorted


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

arr = [12, 11, 13, 5, 6]
print(insertion_sort(arr))
