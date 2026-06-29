class Solution:
    def jump(self, nums: List[int]) -> int:
        # The obvious greedy soltuion here is to test all possiblites and return
        # the smallest number from a given path. So if nums[i] is 4 we do 4 reursive calls to
        # find paths from each jump length 1-4.
        leastJumps = 100
        def findFewestJumps(index, jumps):
            nonlocal leastJumps
            if index >= len(nums) - 1:
                if jumps < leastJumps:
                    leastJumps = jumps
                return
            
            for jump in range(1, nums[index] + 1):
                findFewestJumps(index + jump, jumps + 1)

        
        findFewestJumps(0, 0)
        return leastJumps