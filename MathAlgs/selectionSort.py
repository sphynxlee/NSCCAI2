list = [7, 1, 4, 2, 3, -1]

def selection_sort(list):
    for i in range(len(list)):
        min_index = i
        for j in range(i+1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
        list[i], list[min_index] = list[min_index], list[i]
    return list

print(selection_sort(list))

# Through the whole process of the selection sort, I figured out that the key principle is we should iterate the whole list on its length, and in every iteration, we try to find out the minimum value's index and then let the minimum to the left of the list, and then we do the comparison of the rest of the list.
# [-1, 1, 4, 2, 3, 7]
# [-1, 1, 2, 4, 3, 7]
# [-1, 1, 2, 3, 4, 7]
