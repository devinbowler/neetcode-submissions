class MedianFinder:

    def __init__(self):
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        #minHeap = self.arr.copy()
        #heapq.heapify(minHeap)
        curList = self.arr.copy()
        curList.sort()
        print(curList)
        n = len(curList)
        if n < 3:
            mid = 0
        else:
            mid = (n//2) - 1
        if n % 2 == 0:
            avg = (curList[mid] + curList[mid + 1]) / 2
            return avg
        else:
            return curList[n//2]
        