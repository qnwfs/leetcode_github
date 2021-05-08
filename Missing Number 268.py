def missingNumber(nums):
    nums.sort()
    a = [i for i in range(len(nums)+1)]
    a = set(a)
    nums = set(nums)
    x = a - nums
    for i in x:
        return i

nums = [1]
print(missingNumber(nums))