def findErrorNums(nums):
    ideal = [i for i in range(1, len(nums)+1)]
    di = {}
    final = []
    for i in nums:
        if i not in di:
            di[i] = 0
            di[i] += 1
        else:
            di[i] += 1
    for i in di.items():
        if i[1] > 1:
            final.append(i[0])
            break
    for i in ideal:
        if i not in di.keys():
            final.append(i)
    return final




nums = [3,2,2]
print(findErrorNums(nums))