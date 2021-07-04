def isPal(x):
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    reverted = 0
    while x > reverted:
        reverted = reverted * 10 + x % 10
        x = x // 10
    return (x == reverted or x == reverted // 10)




x = 121
print(isPal(x))