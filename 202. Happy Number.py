def isHappy(n: int) -> bool:
    checker = set()
    while n != 1:
        n = sum(int(i) ** 2 for i in str(n))
        if n in checker:
            return False
        else:
            checker.add(n)
    else:
        return True


print(isHappy(7))