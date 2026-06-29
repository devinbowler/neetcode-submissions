class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # This problem is a simple search, we can split the array in half
        # and check if the number is higher or lower than the middle digit.
        # We keep doing this split until we have found the target.
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2

            if nums[mid] == target:
                return mid

            elif nums[mid] > target:
                r = mid - 1

            else:
                l = mid + 1
            
        return -1


