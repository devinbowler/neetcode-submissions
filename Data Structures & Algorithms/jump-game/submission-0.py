class Solution:
    def canJump(self, nums: List[int]) -> bool:
        def jump(index):
            if index == len(nums) - 1:
                return True

            stop = nums[index] + index
            for k in range(index + 1, stop + 1):
                if jump(k):
                    return True
            return False

        return jump(0)