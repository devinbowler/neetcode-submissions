class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = False

class WordDictionary:
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = True

        cur.word = True

    def search(self, word: str) -> bool:
        def dfs(root, index):
            cur = root

            for i in range(index, len(word)):
                c = word[i]
                if c == '.':
                    for child in cur.children.values():
                        if dfs(child, i + 1):
                            return True    
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]

            return cur.word


        return dfs(self.root, 0)
        
