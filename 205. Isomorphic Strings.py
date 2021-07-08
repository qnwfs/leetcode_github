def isIsomorphic(s: str, t: str) -> bool:
    """
    Устанавливаем соответствие между символами строк,
    проверям находятся ли они на правильных местах
    """
    if len(s) != len(t):
        return False
    else:
        values = {}
        positions = {}
        for i in range(len(s)):
            if s[i] not in values.keys():
                if t[i] not in values.values():
                    values[s[i]] = t[i]
        for i in t:
            if i not in values.values():
                return False
        for i in s:
            if i not in values.keys():
                return False
        for i in range(len(s)):
            positions[i] = s[i]
        for key, value in positions.items():
            if values[value] != t[key]:
                return False
        return True


s = "badc"
t = "baba"
print(isIsomorphic(s, t))