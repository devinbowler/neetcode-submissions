class Solution:
    def trap(self, height: List[int]) -> int:
        
        # We track each given postion in the array and use two pointers
        # to keep track of the max bar of both the right and left we then use
        # the equations 'min(Left, Right) - h[i]' to find how much water at that
        # given spot we can have. Because as long as there is a border taller than
        # the current spot on both sides we can fill some water it just depends on
        # the current height - current height.

        if not height:
            return 0

        l, r = 0, len(height) - 1
        leftMax, rightMax = height[l], height[r]
        res = 0
        while l < r:
            if leftMax < rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                res += leftMax - height[l]
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                res += rightMax - height[r]
        return res
        