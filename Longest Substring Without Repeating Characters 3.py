def lengthOfLongestSubstring(s: str):
    temp = ''
    maks = 0
    for i in s:
        if i not in temp:
            temp += i
            maks = max(len(temp), maks)
        else:
            temp = temp[temp.find(i)+1:] + i
    return maks


s = " "
print(lengthOfLongestSubstring(s))