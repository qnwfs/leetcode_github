class Solution:
    def checkRecord(self, s: str) -> bool:
        a_counter = 0
        l_checker = 0
        for i in range(len(s)):
            if s[i] != 'L':
                l_checker = 0
            if s[i] == "A":
                a_counter += 1
                if a_counter >= 2:
                    return False
            if s[i] == 'L':
                l_checker += 1
                if l_checker >= 3:
                    return False
        return True