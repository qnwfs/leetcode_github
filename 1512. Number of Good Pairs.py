def numIdenticalPairs(nums) -> int:
    dict = {}
    total = 0
    for i in range(len(nums)):
        if nums[i] not in dict:
            dict[nums[i]] = 0
            dict[nums[i]] += 1
        else:
            dict[nums[i]] += 1
    for i in dict:
        if dict[i] > 1:
            total += (dict[i] * (dict[i] - 1) // 2)
    return total


nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))