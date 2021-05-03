def plusOne(digits: list):
    if digits[-1] == 9:
        if len(digits) == 1:
            return [1, 0]
        return plusOne(digits[:-1]) + [0]
    else:
        digits[-1] += 1
    return digits



nums = [1,4,9,9]
print(plusOne(nums))