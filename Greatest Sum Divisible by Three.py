def maxSumDivThree(nums: list):
    not_div_by_3 = []
    total = 0
    max_sum = 0
    for i in nums:
        if i % 3 == 0:
            total += i
        else:
            not_div_by_3.append(i)
    not_div_by_3  = sorted(not_div_by_3)
    for i in not_div_by_3:
        total += i
    q = 0
    while total % 3 != 0 and q < len(not_div_by_3):
        total -= not_div_by_3[q]
        q += 1
    return total




nums = [1,2,3,4,4]
print(maxSumDivThree(nums))

