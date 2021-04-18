def SortArrayByParity(A):
    odd_list = list()
    even_list = list()
    final_list = list()
    for i in A:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    for i in even_list:
        final_list.append(i)
    for j in odd_list:
        final_list.append(j)
    return final_list



A = [3,1,2,4]
print(SortArrayByParity(A))