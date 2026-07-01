class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for step in range(k):
            nums[:] = [nums[-1]] + nums[:len(nums) - 1]