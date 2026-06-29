class Solution:
    def climbStairs(self, n: int) -> int:
        totalWays = 0

        def stairs(cur, total):
            nonlocal totalWays
            total += cur
            if total == n:
                totalWays += 1
                return 
            if total > n:
                return

            stairs(1, total)
            stairs(2, total)

        stairs(0, 0)
        return totalWays