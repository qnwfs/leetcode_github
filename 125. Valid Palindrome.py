import re

def isPalindrome(s: str):
    s = re.sub(r"[^a-z0-9]", "", s.lower())
    return s == s[::-1]

