def isPowerOfTwo(n: int) -> bool:
    if n == 0:
        return False
    n = bin(n)[2:]
    if n[0] == '1':
        for i in n[1:]:
            if i != '0':
                return False
        else:
            return True
    return False

print(isPowerOfTwo(2))
