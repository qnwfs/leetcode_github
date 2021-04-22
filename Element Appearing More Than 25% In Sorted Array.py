def findSpecialInteger(arr: list):
    maxc = 0
    max = 0
    for i in arr:
        if arr.count(i) >= maxc:
            maxc = arr.count(i)
            max = i
    if maxc >= len(arr)/4:
        return max
    else:
        return None

arr = [6700,8858,8858,8858,8858]
print(findSpecialInteger(arr))