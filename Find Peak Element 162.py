class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
        else:
            return len(nums)-1