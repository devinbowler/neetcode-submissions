# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
            
        self.max_diameter = 0  # Store the global maximum diameter
        
        def height(node):
            if node is None:
                return 0  # Base case: height of an empty tree is 0
            
            # Recursively calculate the height of the left and right subtrees
            left_height = height(node.left)
            right_height = height(node.right)
            
            # Calculate the diameter of the current node (path through left + right)
            current_diameter = left_height + right_height
            
            # Update the maximum diameter seen so far
            self.max_diameter = max(self.max_diameter, current_diameter)
            
            # Return the height of this subtree to its parent
            return 1 + max(left_height, right_height)
        
        height(root)  # Call the recursive function starting from the root
        return self.max_diameter  # Return the global maximum diameter