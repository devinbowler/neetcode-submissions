class Solution:
    def climbStairs(self, n: int) -> int:
        totalWays = 0

        def stairs(total):
            nonlocal totalWays
            if total == n:
                totalWays += 1
                return 
            if total > n:
                return

            stairs(total + 1)
            stairs(total + 2)

        stairs(0)
        return totalWays