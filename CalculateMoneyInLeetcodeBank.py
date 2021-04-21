def totalMoney(n):
    weeks = n//7
    if n%7 != 0:
        weeks += 1
    days = 0
    total = 0
    for i in range(1, weeks+1):
        for j in range(7):
            total += i+1*j
            days += 1
            if days >= n:
                return total
                break

n = 20
print(totalMoney(n))
