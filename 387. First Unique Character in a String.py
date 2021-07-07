def firstUniqChar(s: str) -> int:
    dict = {}
    for i in s:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for key, item in dict.items():
        if item == 1:
            return s.index(key)
    return -1

s = "aabb"
print(firstUniqChar(s))

