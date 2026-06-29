class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # This problem uses an algorithm that loops through the list of heights
        # and makes a stack to keep track of tuple pairs of heights and index.
        # We have a loop that goes through the list of heights, and checks
        # if the current height is less than the last added height, if so, we will pop
        # the last height and calculate its area and updated maxArea if it is bigger
        # than the current maxArea, and set our last index of smallest, represente as 
        # 'start'. Otherwise we just append the current height and index. Lastly, if there
        # are left of heights in the list, we go through them, and calculate their areas,
        # and check if any of them are greater than current maxArea.

        stack = [] # pair: (index, height)
        maxArea = 0
        for i, h in enumerate(heights): 
            start = i
            while stack and stack[-1][1] > h: # stack[-1][1] is top elements (-1) and height (index 1)
                index, height = stack.pop()
                maxArea = max(maxArea, (height * (i - index)))
                start = index
            stack.append((start, h))

        for i, h in stack:
            maxArea = max(maxArea, h * (len(heights) - i))

        return maxArea