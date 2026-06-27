class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxCount = 0
        currentCount = 0
        i=0
        while i < len(nums):
            if nums[i] == 1:
                currentCount += 1
                i += 1
            elif nums[i] == 0:
                maxCount = max(maxCount, currentCount)
                currentCount = 0
                i += 1
        return max(maxCount, currentCount)