def checkRecord(s):
    check = {'A': 0, 'L': 0, 'P': 0}
    consecutive_alarm = 0
    for i in s:
        if i == "L":
            consecutive_alarm += 1
            if consecutive_alarm == 3:
                return False
        else:
            consecutive_alarm = 0
        check[i] += 1
    if check["A"] < 2:
        return True


s = "PPALLL"
print(checkRecord(s))