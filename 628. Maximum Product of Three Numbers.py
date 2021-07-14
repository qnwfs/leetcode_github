def maximumProduct(nums):
    nums = sorted(nums, reverse=True)
    max1 = nums[0]
    max2 = nums[1]
    max3 = nums[2]
    min1 = nums[-1]
    min2 = nums[-2]
    if min1 * min2 > max2 * max3 and max1 > 0:
        return max1*min1*min2
    else:
        return max1*max2*max3


nums = [-100,-98,-1,2,3,4]
print(maximumProduct(nums))