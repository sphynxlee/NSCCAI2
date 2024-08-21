def maxSubArray(nums):
    maxSub = nums[0]
    currentSub = nums[0]
    for i in range(1, len(nums)):
        currentSub = max(nums[i], currentSub + nums[i])
        maxSub = max(maxSub, currentSub)
    return maxSub

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(maxSubArray(nums))  # 6