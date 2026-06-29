class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        returnArray = []

        def findWord(x, y, word, index, visited):
            # Check if we already computed this state
            if index == len(word):  # Successfully found the word
                return True

            if (x < 0 or x >= cols or y < 0 or y >= rows or
                board[y][x] != word[index] or (x, y) in visited):
                return False

            visited.add((x, y))
            
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in directions:
                if findWord(x + dx, y + dy, word, index + 1, visited):
                    return True


            visited.remove((x, y))
            return False  # Word not found in this path
        
        def helpFind(word):
            nonlocal returnArray
            for row in range(rows):
                for col in range(cols):
                    if board[row][col] == word[0]:
                        if findWord(col, row, word, 0, set()):
                            returnArray.append(word)
                            return

        for word in words:
            helpFind(word)

        return returnArray