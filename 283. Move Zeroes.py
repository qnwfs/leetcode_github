def moveZeroes(nums) -> None:
    zero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[zero] = nums[zero], nums[i]
            zero += 1
    return nums
    """
    Берём индекс нуля и как только попадаем на ненулевое число - меняем местами с нулём.
    zero в счетчике прибавляется если число не ноль. Таким образом мы тащим все нули вправо
    """

nums = [1, 0, 0, 2, 0]
print(moveZeroes(nums))