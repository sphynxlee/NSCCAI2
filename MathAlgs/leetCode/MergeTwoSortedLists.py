def merge_two_sorted_lists(list1, list2):
    min_list = list1 if len(list1) < len(list2) else list2
    max_list = list1 if len(list1) > len(list2) else list2

    merge_list = []
    for i in range(len(min_list)):
        if list1[i] < list2[i]:
            merge_list.append(list1[i])
            merge_list.append(list2[i])
        else:
            merge_list.append(list2[i])
            merge_list.append(list1[i])

    for i in range(len(min_list), len(max_list)):
        merge_list.append(max_list[i])

    return merge_list

list1 = [1, 2, 4]
list2 = [1, 3, 4, 5]
print(merge_two_sorted_lists(list1, list2))  # [1, 1, 2, 3, 4, 4, 5]