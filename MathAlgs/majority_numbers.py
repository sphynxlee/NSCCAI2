def majority_element(nums):
    count_dict = {}

    for num in nums:
        if num in count_dict:
            count_dict[num] += 1
        else:
            count_dict[num] = 1

    n = len(nums)
    for key, value in count_dict.items():
        if value > n / 2:
            return key

    return "No majority element"

# Example usage:
A = [3, 3, 4, 2, 4, 4, 2, 4, 4]
result = majority_element(A)
print(result)
