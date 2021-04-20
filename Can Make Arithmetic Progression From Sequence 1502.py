def canMakeArithmeticProgression(nums):
    nums.sort()
    znam = nums[1]-nums[0]
    i = 0
    while i < len(nums) - 1:
        if nums[i] + znam != nums[i+1]:
            return False
            break
        else:
            i += 1
    else:
        return True


arr = [1,2,4]
print(canMakeArithmeticProgression(arr))