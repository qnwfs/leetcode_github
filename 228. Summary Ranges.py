def getStr(first, last):
    return str(first) if first == last else f"{first}->{last}"

def summaryRanges(nums):
    if len(nums) == 0:
        return nums
    res = []
    first = nums[0]
    for i in range(1, len(nums)):
        if nums[i - 1] + 1 != nums[i]:
            res.append(getStr(first, nums[i - 1]))
            first = nums[i]
    res.append(getStr(first, nums[-1]))
    return res


nums = [0,1,2,4,5,7]
print(summaryRanges(nums))