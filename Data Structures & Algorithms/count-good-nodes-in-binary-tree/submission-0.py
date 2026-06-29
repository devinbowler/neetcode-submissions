# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        numOfGood = 0

        if root is None:
            return 0
        else:
            numOfGood = 1
        
        def checkNodes(node, maxVal):
            nonlocal numOfGood
            if node is None:
                return numOfGood

            right = node.right
            left = node.left 

            if left is not None:
                if left.val >= maxVal:
                    numOfGood += 1
                    checkNodes(left, left.val)
                else:
                    checkNodes(left, maxVal)

            if right is not None:
                if right.val >= maxVal:
                    numOfGood += 1
                    checkNodes(right, right.val)
                else:
                    checkNodes(right, maxVal)

            
        checkNodes(root, root.val)

        return numOfGood

            