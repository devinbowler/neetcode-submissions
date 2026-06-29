class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        tracked = []
        for each in nums:
            if each in tracked:
                tracked.remove(each)
            else:
                tracked.append(each)

        return tracked[0]