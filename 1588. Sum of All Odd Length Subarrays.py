def sumOddLengthSubarrays(arr) -> int:
    ans = 0
    prefixSum = [0]
    for num in arr:
        prefixSum.append(prefixSum[-1] + num)
    for i in range(1, len(arr) + 1, 2):
        for j in range(i - 1, len(arr)):
            ans += prefixSum[j + 1] - prefixSum[j + 1 - i]
    return ans


arr = [1, 4, 2, 5, 3]
print(sumOddLengthSubarrays(arr))