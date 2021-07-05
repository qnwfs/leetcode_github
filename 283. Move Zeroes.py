def moveZeroes(nums) -> None:
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums

nums = [0, 1, 0, 3, 12]
print(moveZeroes(nums))