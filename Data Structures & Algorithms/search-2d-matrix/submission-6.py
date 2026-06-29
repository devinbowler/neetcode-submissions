class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top, bot = 0, rows - 1
        while top <= bot:
            midRow = (top + bot) // 2

            if(target > matrix[midRow][-1]):
                top = midRow + 1
            elif(target < matrix[midRow][0]):
                bot = midRow - 1
            else:
                break

        if not (top <= bot):
            return False
        selectRow = (top + bot) // 2
        left, right = 0, cols - 1
        while left <= right:
            middle = left + (right - left) // 2
            if target > matrix[selectRow][middle]:
                left = middle + 1
            elif target < matrix[selectRow][middle]:
                right = middle - 1
            else:
                return True

        return False