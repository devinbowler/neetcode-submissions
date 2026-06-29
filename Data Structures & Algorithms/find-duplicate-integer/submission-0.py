class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        seenValues = []
        for i in nums: 
            if i in seenValues:
                return i
            else: 
                seenValues.append(i)