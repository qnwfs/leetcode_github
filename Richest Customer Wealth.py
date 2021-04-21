def maxWealth(accounts: list):
    max = 0
    for i in accounts:
        summa = sum(i)
        if summa > max:
            max = summa
    return max

accounts = [[2,8,7],[7,1,3],[1,9,5]]
print(maxWealth(accounts))