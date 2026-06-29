class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.map = [[] for _ in range(self.size)]
        

    def put(self, key: int, value: int) -> None:
        bucket = key % self.size;
        for i, (k, v) in enumerate(self.map[bucket]):
            if k == key:
                self.map[bucket][i] = (key, value)
                return
        
        self.map[bucket].append((key, value))

        

    def get(self, key: int) -> int:
        bucket = key % self.size;
        for i, (k, v) in enumerate(self.map[bucket]):
            if k == key:
                return v
        return -1
        

    def remove(self, key: int) -> None:
        bucket = key % self.size;
        for i, (k, v) in enumerate(self.map[bucket]):
            if k == key:
                del self.map[bucket][i]
                return

        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)