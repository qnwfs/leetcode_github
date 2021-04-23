def countCharacters(words: list, chars: str):
    sum = 0
    for i in words:
        for j in i:
            if j not in chars:
                break
            elif i.count(j) > chars.count(j):
                break
        else:
            sum += len(i)
    return sum


words = ["hello","e","leeetcode"]
chars = "welldonehoneyr"
print(countCharacters(words,chars))