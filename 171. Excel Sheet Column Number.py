def titleToNumber(col: str) -> int:
    if len(col) == 0:
        return 0
    if len(col) == 1:
        return ord(col[0]) - 64
    total = 0
    for i in col:
        total *= 26
        total += ord(i) - 64
    return total

col = 'AAA'
print(titleToNumber(col))