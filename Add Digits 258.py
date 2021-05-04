def addDigits(num: int):
    summa = 0
    while num > 0:
        summa += num % 10
        num = num // 10
    if summa < 9:
        return summa
    else:
        num = summa
        return addDigits(num)


num = 0
print(addDigits(num))