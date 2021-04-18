def SortArrayByParityII(nums):
    even_list = []
    odd_list = []
    even = 0
    odd = 0
    final_list = []
    for i in nums:
        if i % 2 == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    for i in range(len(odd_list)+len(even_list)):
        if i % 2 == 0:
            if even >= len(even_list):
                final_list.append(odd_list[odd])
                odd += 1
            else:
                final_list.append(even_list[even])
                even += 1
        if i % 2 != 0:
            if odd >= len(odd_list):
                final_list.append(even_list[even])
                even += 1
            else:
                final_list.append(odd_list[odd])
                odd += 1
    return final_list

nums = [2,3]
print(SortArrayByParityII(nums))