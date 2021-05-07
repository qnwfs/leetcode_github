def maxNumberOfBalloons(text: str):
    target = 'balloon'
    checker = {}
    array = []
    for i in target:
        checker[i] = 0
    for i in text:
        if i in target:
            checker[i] += 1
    checker["l"] /= 2
    checker['o'] /= 2
    for i in checker.values():
        array.append(i)
    return int(min(array))

text = "ballloonbanba"
print(maxNumberOfBalloons(text))