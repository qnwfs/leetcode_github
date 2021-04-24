def relativeSortArray(arr1: list, arr2: list):
    final = list();
    for i in arr2:
        for _ in range(arr1.count(i)):
            final.append(i)
    arr1.sort()
    for i in arr1:
        if i not in final:
            for _ in range(arr1.count(i)):
                final.append(i)
    return final


arr1 = [2,21,43,38,0,42,33,7,24,13,12,27,12,24,5,23,29,48,30,31]
arr2 = [2,42,38,0,43,21]
print(relativeSortArray(arr1,arr2))