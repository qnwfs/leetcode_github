def canBeEqual(arr, target):
    arr = sorted(arr)
    target = sorted(target)
    if arr == target:
        return True
    else:
        return False

