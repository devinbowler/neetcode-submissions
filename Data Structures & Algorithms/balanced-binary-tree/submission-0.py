# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Recursively check each node if it has children, if not
        # the height is 0, if it does the height is 1, at each node
        # we want to check 1 + max(left.height, right.height).
        if root is None:
            return True

        def findDepth(node):
            if node is None:
                return 0  # Return 0 instead of None for an empty node
            
            # Recursively calculate depth of left and right subtrees
            left_depth = findDepth(node.left)
            right_depth = findDepth(node.right)
            
            # Check for imbalance and propagate it up the recursion
            if left_depth == -1 or right_depth == -1 or abs(left_depth - right_depth) > 1:
                return -1  # Return -1 as a signal that the tree is unbalanced
            
            # Return the maximum of the two depths + 1 for the current node
            return max(left_depth, right_depth) + 1

        # Calculate the depth for the entire tree and check for imbalance
        return findDepth(root) != -1