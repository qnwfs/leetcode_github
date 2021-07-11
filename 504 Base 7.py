def convertToBase7(num: int) -> str:
    total = ''
    otr = False
    if num == 0:
        return '0'
    if num < 0:
        otr = True
        num = num * (-1)
    while num > 0:
        total += str(num % 7)
        num = num // 7
    if otr:
        return '-' + total[::-1]
    else:
        return total[::-1]

num = 7
print(convertToBase7(num))