class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seenValues = set()
        for i in nums: 
            if i in seenValues:
                return i
            else: 
                seenValues.add(i)
