class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # This problem is a simple search, we can split the array in half
        # and check if the number is higher or lower than the middle digit.
        # We keep doing this split until we have found the target.
        for i in range(len(nums)):
            if (nums[i] == target):
                return i


        return -1