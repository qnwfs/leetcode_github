def findDuplicates(nums: list):
    dupl = {}
    lisp = []
    for i in nums:
        if i not in dupl:
            dupl[i] = 1
        else:
            dupl[i] = 2

    for key in dupl.keys():
        if dupl[key] == 2:
            lisp.append(key)
    return sorted(lisp)


nums = [1]
print(findDuplicates(nums))