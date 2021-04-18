def sortArrayByParityII(A):
    N = len(A)
    ans = [None] * N #создаем массив размера N, заполненный NUllами
    print(ans)
    t = 0
    for i, x in enumerate(A):#enumerate перебирает сразу строку и элемент
        if x % 2 == 0:
            ans[t] = x
            t += 2

    t = 1
    for i, x in enumerate(A):
        if x % 2 == 1:
            ans[t] = x
            t += 2

    # We could have also used slice assignment:
    # ans[::2] = (x for x in A if x % 2 == 0)
    # ans[1::2] = (x for x in A if x % 2 == 1)

    return ans

nums = [123,421124,241,24,1124,12,241]
print(sortArrayByParityII(nums))