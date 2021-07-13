class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        n = str(n)
        prod = int(n[0])
        summ = sum(int(i) for i in n)
        for i in n[1::]:
            prod = prod * int(i)
        return prod - summ