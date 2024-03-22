# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2]

def removeElement(nums, val):
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return (i, nums[:i])

nums = [3,2,2,3]
val = 3
print(removeElement(nums, val))