def findDisappearedNumbers(nums: list):
    a = set(i for i in range(1, len(nums)+1))
    b = set(nums)
    return a - b

nums = [4,3,2,7,8,2,3,1]
print(findDisappearedNumbers(nums))