# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        def findDepth(node):
            if node is None:
                return 0  # Base case: return 0 at leaf nodes
            
            # Recursively calculate depth of left and right subtrees
            left_depth = findDepth(node.left)
            right_depth = findDepth(node.right)
            
            # Return the maximum of the two depths + 1 for the current node
            return max(left_depth, right_depth) + 1

        # Calculate the depth for both left and right subtrees from the root
        left_depth = findDepth(root.left)
        right_depth = findDepth(root.right)

        # Print the depths of both sides
        print(f"Left depth: {left_depth}, Right depth: {right_depth}")

        # Return the maximum depth of the entire tree
        return max(left_depth, right_depth) + 1

