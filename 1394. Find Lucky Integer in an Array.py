class Solution:
    def findLucky(self, arr: List[int]) -> int:
        dict = {}
        for i in arr:
            if i not in dict:
                dict[i] = 0
                dict[i] += 1
            else:
                dict[i] += 1
        max = 0
        for i in dict.items():
            if i[0] == i[1] and i[0] > max:
                max = i[0]
        if max == 0:
            return -1
        else:
            return max