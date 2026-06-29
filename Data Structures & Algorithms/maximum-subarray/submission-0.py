class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = float('-inf')
        for start in range(len(nums)):
            currentSum = 0
            for end in range(start, len(nums)):
                currentSum += nums[end]
                maxSum = max(currentSum, maxSum)

        return maxSum