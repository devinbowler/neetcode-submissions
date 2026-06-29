class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        returnArray = []

        def findWord(x, y, curWord, index, visited):
            # Check if we already computed this state
            if index == len(curWord):  # Successfully found the word
                return True

            if (x < 0 or x >= cols or y < 0 or y >= rows or
                board[y][x] != curWord[index] or (x, y) in visited):
                return False

            visited.add((x, y))
            
            directions = [(0,1), (0,-1), (1,0), (-1,0)]
            for dx, dy in directions:
                if findWord(x + dx, y + dy, curWord, index + 1, visited):
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


        helpFind(word)
        print(returnArray)
        if len(returnArray) > 0:
            return True
        else:
            return False