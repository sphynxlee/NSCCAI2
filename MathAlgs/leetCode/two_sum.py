def two_sum(nums, target):
    # create a dictionary to store the value and index
    dict = {}
    # loop through the list
    for i in range(len(nums)):
        # if the target minus the current value is in the dictionary
        if target - nums[i] in dict:
            # return the index of the target minus the current value and the current index
            return [dict[target - nums[i]], i]
        # else add the current value and index to the dictionary
        else:
            dict[nums[i]] = i
    # if no solution is found return an empty list
    return []

lists = [2, 7, 11, 15]
target = 9
print(two_sum(lists, target))


def two_sum2(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[j] == target - nums[i]:
                return [i, j]
    return []

lists = [2, 7, 11, 15]
target = 18
print(two_sum2(lists, target))


def two_sum3(array, target):
    for i in range(0, len(array)-1):
        for j in range(0, len(array)-1):
            if i == j:
                continue
            elif array[i] + array[j] == target:
                return i, j
    return -1

# test:
arr = [2, 7, 11, 15]
target = 13
print("Indices:", two_sum3(arr, target))