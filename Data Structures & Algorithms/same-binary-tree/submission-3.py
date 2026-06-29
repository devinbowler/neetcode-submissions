# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        treeOne = []
        treeTwo = []

        def checkTree(node, tree):
            if node is None:
                return
            currentVal = node.val
            leftNode = node.left
            rightNode = node.right
            if leftNode and rightNode is not None:
                print("Node and leafs: ", currentVal, node.left.val, node.right.val)

            tree.append(currentVal)
            if leftNode is not None:
                checkTree(leftNode, tree)
            else:
                tree.append(None)
            if rightNode is not None:
                checkTree(rightNode, tree)
            else:
                tree.append(None)


        checkTree(p, treeOne)
        checkTree(q, treeTwo)
        print(treeOne, treeTwo)

        if treeOne == treeTwo:
            return True


        return False