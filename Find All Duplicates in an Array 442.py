def findDuplicates(nums: list):
    x = set()
    lisp = []
    for i in nums:
        if i in x:
            lisp.append(i)
        else:
            x.add(i)
    return lisp


nums = [1,2,3,4,5,6,7,7]
print(findDuplicates(nums))