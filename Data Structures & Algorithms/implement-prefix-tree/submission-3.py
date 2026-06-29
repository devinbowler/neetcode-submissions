class PrefixTree:

    def __init__(self):
        self.array = []

    def insert(self, word: str) -> None:
        self.array.append(word)

    def search(self, word: str) -> bool:
        if word in self.array:
            return True
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        for word in self.array:
            print(word)
            if word.startswith(prefix):
                return True
        
        return False
        