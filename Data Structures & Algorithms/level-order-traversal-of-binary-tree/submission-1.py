# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levelDict = {}

        returnTree = []
        def formTree(node, level):
            if node is None:
                return

            if level in levelDict:
                levelDict[level].append(node.val) 
            else:
                levelDict[level] = [node.val]
            
            curr = node.val
            left = node.left
            right = node.right

            if left is not None:
                formTree(left, level + 1)

            if right is not None:
                formTree(right, level + 1)


        formTree(root, 1)

        for index in range(1, len(levelDict) + 1):
            returnTree.append(levelDict[index])

        print(returnTree)

        return returnTree