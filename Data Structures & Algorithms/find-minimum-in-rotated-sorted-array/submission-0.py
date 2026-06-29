class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = 100
        for i in nums:
            if (i < res):
                res = i

        return res    