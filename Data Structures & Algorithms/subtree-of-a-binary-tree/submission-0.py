# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Helper function to check if two trees are identical
        def isIdentical(node1, node2):
            if not node1 and not node2:  # Both trees are None
                return True
            if not node1 or not node2:  # One tree is None but the other is not
                return False
            if node1.val != node2.val:  # Values of the nodes do not match
                return False
            
            # Check left and right subtrees recursively
            return isIdentical(node1.left, node2.left) and isIdentical(node1.right, node2.right)
        
        # Main function to traverse the main tree to look for a subtree match
        def checkRoot(node):
            if node is None:
                return False
            
            # Check if the current subtree matches subRoot
            if isIdentical(node, subRoot):
                return True
            
            # Otherwise, keep searching in the left and right subtrees
            return checkRoot(node.left) or checkRoot(node.right)
        
        return checkRoot(root)
