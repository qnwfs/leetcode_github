def uncommonFromSentences(A: str, B: str):
    total = []
    xa = A.split()
    xb = B.split()
    for i in xa:
        if xa.count(i) == 1 and xb.count(i) == 0:
            total.append(i)
    for i in xb:
        if xb.count(i) == 1 and xa.count(i) == 0:
            total.append(i)
    return total


A = "this apple is sweet"
B = "this apple is sour"
print(uncommonFromSentences(A,B))

