class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # The idea here is to find a rate that finishes each stack
        # in 'h' iterations and the smallest rate of such. 

        left, right = 1, max(piles)
        res = right

        while left <= right:
            k = (left + right) // 2
            totalTime = 0

            for p in piles:
                totalTime += math.ceil(float(p) / k)
            if totalTime <= h:
                res = k
                right = k - 1
            else:
                left = k + 1
        return res
                