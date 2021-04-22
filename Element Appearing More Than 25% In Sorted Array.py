import collections

def findSpecialInteger(arr: list):
    x = collections.Counter(arr)
    return x.most_common()[0][0]

arr = [6700,8858,8858,8858,8858]
print(findSpecialInteger(arr))