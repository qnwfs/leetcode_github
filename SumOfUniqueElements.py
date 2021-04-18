from collections import Counter
def sumOfUnique(nums):
    a = Counter(nums)
    x = a.most_common()
    sum = 0
    for i in x:
        if i[1] == 1:
            sum += i[0]
    return sum

nums = [1,1,1,1,1]
print(sumOfUnique(nums))

#testing git commits 2