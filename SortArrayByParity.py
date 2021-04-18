def SortArrayByParity(A):
    A.sort(key=lambda x: x % 2)
    return A



A = [3,1,2,4]
print(SortArrayByParity(A))