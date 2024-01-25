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