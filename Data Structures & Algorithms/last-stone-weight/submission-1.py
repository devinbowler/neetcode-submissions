class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones.sort()
        stones.reverse()
        for index in range(len(stones)):
            if len(stones) is 1:
                return stones[0]
            elif stones == []:
                return 0
            print(stones, index)
            if stones[0] == stones[1]:
                stones = stones[2:]
            elif stones[0] > stones[1]:
                newWeight = stones[0] - stones[1]
                stones = stones[2:]
                stones.insert(0, newWeight)
                stones.sort()
                stones.reverse()
            
        return stones[0]

