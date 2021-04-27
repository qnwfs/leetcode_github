def containsNearbyDuplicate(nums, k):
    dic = {}
    for i, v in enumerate(nums):
        if v in dic and i - dic[v] <= k:
            return True
        dic[v] = i
    return False


nums = [3, 2, 4, 5, 1, 1]
k = 2
print(containsNearbyDuplicate(nums, k))