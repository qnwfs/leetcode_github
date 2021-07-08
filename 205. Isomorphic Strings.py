def isIsomorphic(s: str, t: str) -> bool:
    mydict = dict()
    val = "" #сохраняет буквы второго слова, которые уже сопоставлены с буквами из первого
    for i in range(len(s)):
        if s[i] not in mydict:
            if t[i] not in val:
                mydict[s[i]] = t[i]
                val += t[i]
            else:
                return False
        else:
            if mydict[s[i]] != t[i]:
                return False
    return True


s = "badc"
t = "baba"
print(isIsomorphic(s, t))
