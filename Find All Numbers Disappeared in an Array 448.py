def findDisappearedNumbers(nums: list):
    nums.sort()
    finale = []
    for i in range(0, len(nums)-1):
        if nums[i] + 1 != nums[i+1]:
            finale.append(nums[i]+1)
    return finale

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))