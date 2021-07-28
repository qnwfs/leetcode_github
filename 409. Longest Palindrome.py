class Solution:
    def longestPalindrome(self, s: str) -> int:
        dict = {}
        total = 0
        for i in s:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1
        possible_center = 0
        possible_center_with_1_symbol = 0
        for key, value in dict.items():
            if value % 2 == 0:
                total += value
            else:
                possible_center = 1
                total += value - 1
        if total % 2 == 0 and possible_center:
            return total + 1
        else:
            return total