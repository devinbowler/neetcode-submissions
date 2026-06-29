# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        elementArr = []
        def makeArr(node):
            if node is None:
                return
            
            curr = node.val
            left = node.left
            right = node.right

            elementArr.append(curr)

            if left is not None:
                makeArr(left)
            if right is not None:
                makeArr(right)


        makeArr(root)

        sortedArr = sorted(elementArr)

        print(sortedArr)
        result = 0
        for index in range(k + 1):
            print(index, k)
            if index == k:
                result = int(sortedArr[index - 1])

        return result