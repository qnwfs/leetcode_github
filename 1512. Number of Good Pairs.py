def numIdenticalPairs(nums) -> int:
    pairs = 0
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for num in d:
        val = d[num]
        for i in range(val):
            pairs += i
    return pairs


nums = [1,2,3,1,1,3]
print(numIdenticalPairs(nums))