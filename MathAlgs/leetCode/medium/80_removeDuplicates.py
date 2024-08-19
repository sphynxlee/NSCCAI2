# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3]

def removeDuplicates(nums):
    i = 0
    for j in range(len(nums)):
        if i < 2 or nums[j] != nums[i-2]:
            nums[i] = nums[j]
            i += 1
    return (i, nums[:i])

nums = [1,1,1,2,2,3]
print(removeDuplicates(nums))