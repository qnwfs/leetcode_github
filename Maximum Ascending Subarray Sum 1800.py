def maxAscendingSum(nums: list):
    sums = []
    total = nums[0]
    for i in range(len(nums)-1):
        if nums[i+1] > nums[i]:
            total += nums[i+1]
        else:
            sums.append(total)
            total = nums[i+1]
    sums.append(total)
    return max(sums)

nums = [100,10,1]
print(maxAscendingSum(nums))
