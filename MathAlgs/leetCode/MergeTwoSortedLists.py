def merge_two_sorted_lists(list1, list2):
    min_list = list1 if len(list1) < len(list2) else list2
    max_list = list1 if len(list1) > len(list2) else list2
    print('min_list length:', len(min_list))
    print('max_list length:', len(max_list))

    merge_list = []
    for i in range(len(min_list)):
        if list1[i] < list2[i]:
            merge_list.append(list1[i])
            merge_list.append(list2[i])
        else:
            merge_list.append(list2[i])
            merge_list.append(list1[i])
    print('i+1:', i+1)
    for j in range((i+1), len(max_list)):
        merge_list.append(max_list[j])

    return merge_list

list1 = [1, 2, 4]
list2 = [1, 3, 4, 5]
print(merge_two_sorted_lists(list1, list2))  # [1, 1, 2, 3, 4, 4, 5]