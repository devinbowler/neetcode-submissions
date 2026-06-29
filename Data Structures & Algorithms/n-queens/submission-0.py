class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        # Initialize the board as a list of lists
        board = [['.'] * n for _ in range(n)]

        def isSafe(board, row, col):
            # Check vertically up
            for i in range(row):
                if board[i][col] == 'Q':
                    return False
            # Check diagonally up-left
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            # Check diagonally up-right
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            return True

        def dfs(row):
            if row == n:
                # Convert board to the required format
                res.append([''.join(r) for r in board])
                return

            for col in range(n):
                if isSafe(board, row, col):
                    # Place queen
                    board[row][col] = 'Q'
                    # Recurse to the next row
                    dfs(row + 1)
                    # Backtrack by removing the queen
                    board[row][col] = '.'

        dfs(0)
        return res