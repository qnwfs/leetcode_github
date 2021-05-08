def missingNumber(nums):
    expected_sum = len(nums) * (len(nums) + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum


nums = [1]
print(missingNumber(nums))