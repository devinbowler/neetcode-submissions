from functools import lru_cache

class Solution:
    def jump(self, nums: List[int]) -> int:
        # The obvious greedy soltuion here is to test all possiblites and return
        # the smallest number from a given path. So if nums[i] is 4 we do 4 reursive calls to
        # find paths from each jump length 1-4.

        @lru_cache(None)
        def findFewestJumps(index):
            if index >= len(nums) - 1:
                return 0
            
            res = float('inf')
            for jump in range(1, nums[index] + 1):
                res = min(res, 1 + findFewestJumps(index + jump))
            return res

        
        return findFewestJumps(0)