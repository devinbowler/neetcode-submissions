class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        def findRoute():
            start = -1
            for index in range(len(cost)):
                if checkRoute(index):
                    start = index
            
            return start

        def checkRoute(index):
            start = -1
            gasTotal = 0
            for idx in range(index, index + len(cost)):
                idx = idx % len(cost)
                gasTotal += gas[idx]
                gasTotal -= cost[idx]
                if gasTotal < 0:
                    return False
            return True


        startIdx = findRoute()
        return startIdx