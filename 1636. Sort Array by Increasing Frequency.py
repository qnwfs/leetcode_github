from collections import *

def frequencySort(nums):
    dict = Counter()
    total = []
    for i in nums:
        dict[i] += 1
    r = dict.most_common()
    r.sort(key=lambda x: x[0], reverse=True)
    r.sort(key=lambda x: x[1])
    for i in r:
        for j in range(i[1]):
            total.append(i[0])
    return total



nums = [2,3,1,3,2]
print(frequencySort(nums))