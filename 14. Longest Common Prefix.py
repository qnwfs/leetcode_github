def longestCommonPrefix(strs):
    strs = sorted(strs)
    pref = ''
    test_pref = ''
    for i in range(len(strs[0])):
        test_pref += strs[0][i]
        for j in strs:
            if j[i] == strs[0][i]:
                continue
            else:
                return pref
        pref = test_pref
    return pref


strs = ['g']
print(longestCommonPrefix(strs))
