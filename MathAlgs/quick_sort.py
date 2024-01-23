def quick_sort(arr):
    if len(arr) < 2:
        return arr
    else:
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot] # Sub-array of all elements less than the pivot
        greater = [i for i in arr[1:] if i > pivot] # Sub-array of all elements greater than the pivot
        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [10, 5, 2, 3]
print(quick_sort(arr))

# time complexity: O(n log n)
# space complexity: O(n)