def rotateString(self, s: str, goal: str) -> bool:
    if len(s) != len(goal):
        return False
    for i in range(len(s)):
        if s == goal:
            return True
        s += s[0]
        s = s[1:]
    return False

s = 'abcde'
goal = 'cdeab'
print(rotateString(s,goal))