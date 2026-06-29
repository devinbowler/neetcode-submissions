class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # keep a left pointer at 0 and a right pointer starting at 
        # index 2 moving right, compare the left pointer to the 2 right
        # most values, take the highest one and store it in a result
        # array, then move both pointers and repeat until the for loop
        # ends.

        res = []
        leftPoint = 0

        for right in range(k - 1, len(nums)):
            tempRes = float('-inf')
            for left in range(leftPoint, right +1):
                if nums[left] > tempRes:
                    tempRes = nums[left]

            leftPoint += 1
            res.append(tempRes)
        
        return res

