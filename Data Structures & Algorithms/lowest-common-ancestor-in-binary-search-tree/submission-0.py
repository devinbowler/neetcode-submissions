# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        pPath = []
        qPath = []
        
        def findPath(node, target, path):
            if not node:
                return False
            
            # Add the current node to the path
            path.append(node)
            
            # Check if we found the target
            if node.val == target.val:
                return True
            
            # Explore left and right subtrees
            if (node.left and findPath(node.left, target, path)) or \
               (node.right and findPath(node.right, target, path)):
                return True
            
            # Backtrack if the target is not found in either subtree
            path.pop()
            return False
        
        # Find paths to p and q
        findPath(root, p, pPath)
        findPath(root, q, qPath)
        
        # Compare the paths to find the LCA
        lca = None
        for i in range(min(len(pPath), len(qPath))):
            if pPath[i] == qPath[i]:
                lca = pPath[i]
            else:
                break
        
        return lca

        