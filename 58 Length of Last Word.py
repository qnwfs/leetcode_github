def lengthOfLastWord(s):
    s = s.rstrip()
    arr = s.split(' ')
    return len(arr[-1])

s = " "
print(lengthOfLastWord(s))