def isPowerOfFour(n: int) -> bool:
    count = 0
    bit = bin(n)
    bit = str(bit[2::])
    if bit[0] == '1':
        for i in bit[1::]:
            if i == '0':
                count +=1
            else:
                return False
        if count % 2 == 0:
            return True
        else:
            return False
    return False


n = 1
print(isPowerOfFour(n))