class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 0
        check = set()
        while idx < len(nums):
            if nums[idx] not in check:
                check.add(nums[idx])
            else:
                del nums[idx]
                idx -= 1
            
            idx += 1

        return len(nums)