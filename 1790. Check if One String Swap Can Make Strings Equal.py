def areAlmostEqual(s1: str, s2: str) -> bool:
    dict1 = {}
    dict2 = {}
    swap = 0
    sw1 = []
    sw2 = []
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        dict1[i] = s1[i]
    for i in range(len(s2)):
        dict2[i] = s2[i]
    else:
        for i in range(len(dict1)):
            if dict1[i] != dict2[i]:
                sw1.append(dict1[i])
                sw2.append(dict2[i])
                swap += 1
            if swap > 2:
                return False
    if sw1 == sw2[::-1]:
        return True
    else:
        return False

s1 = 'bank'
s2 = 'bank'
print(areAlmostEqual(s1, s2))