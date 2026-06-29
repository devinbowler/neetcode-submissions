class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for each in asteroids:
            while stack and each < 0 and stack[-1] > 0:
                diff = each + stack[-1]
                if diff > 0:
                    each = 0
                elif diff < 0:
                    stack.pop()
                else:
                    each = 0
                    stack.pop()
            if each != 0:
                stack.append(each)

        return stack

