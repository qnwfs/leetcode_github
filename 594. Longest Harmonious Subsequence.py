def findLHS(nums):
    dict = {}
    ans = 0
    for i in nums:
        if i not in dict:
            dict[i] = 1
        else:
            dict[i] += 1
    for i in dict:
        """
        Проверяем все элементы словаря, если в словаре есть элемент, который
        на 1 больше текущего, считаем сумму текущего и большего на один,
        после каждой итерации сравниваем эту сумму с текущим максимумом
        """
        if i + 1 in dict.keys():
            ans = max(ans, dict[i] + dict[i + 1])
    return ans

nums = [1,3,2,2,5,2,3,7]
print(findLHS(nums))