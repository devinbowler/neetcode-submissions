class Solution:
    def climbStairs(self, n: int) -> int:
        totalWays = 0

        def stairs(total):
            nonlocal totalWays
            if total == n:
                totalWays += 1
                return 
            if total > n:
                return  # This prevents unnecessary recursive calls

            # Make two recursive calls to consider climbing 1 or 2 steps
            stairs(total + 1)
            stairs(total + 2)

        # Start with zero steps climbed
        stairs(0)
        return totalWays
