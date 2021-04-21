def checkIfExists(arr: list):
    for i in arr:
        if i == 0:
            if arr.count(0) > 1:
                return True
                break
            else:
                continue
        if 2*i in arr:
            return True
            break
    else:
        return False

arr = [0,0]
print(checkIfExists(arr))