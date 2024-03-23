# quick sort algorithm:
# 1. choose a pivot element from the array
# 2. partition the array into two sub-arrays: elements less than the pivot and elements greater than the pivot
# 3. recursively apply the quick sort algorithm to the sub-arrays
# 4. combine the sorted sub-arrays and the pivot

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less = []
        greater = []

        for x in arr[1:]:
            if x <= pivot:
                less.append(x)
            else:
                greater.append(x)

        return quick_sort(less) + [pivot] + quick_sort(greater)

arr = [10, 5, 2, 3]
print(quick_sort(arr))

# time complexity: O(n log n)
# space complexity: O(n)