def addDigits(num: int):
    sum = 0
    while num > 0:
        sum += num % 10
        num = num // 10
        if num == 0 and sum > 9:
            num = sum
            sum = 0
    return sum


num = 38
print(addDigits(num))