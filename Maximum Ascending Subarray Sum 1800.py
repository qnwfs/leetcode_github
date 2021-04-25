def maxAscendingSum(nums: list):
    total = 0
    lisp = list()
    if len(nums) == 1:
        return nums[0]
    for i in range(len(nums)-1):
        if nums[i] < nums[i+1]:
            total += nums[i]
        else:
            total += nums[i]
            lisp.append(total)
            total = 0
    if nums[len(nums) - 1] > nums[len(nums) - 2]:
        total += nums[len(nums) - 1]
        lisp.append(total)
    else:
        lisp.append(total)
    lisp.sort(reverse=True)
    return lisp[0]


nums = [100,10,1]
print(maxAscendingSum(nums))
