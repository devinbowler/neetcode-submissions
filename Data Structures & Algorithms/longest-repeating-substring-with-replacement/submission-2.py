class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        res = 0
        left = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            res = max(res, count[s[r]])

            if (r - left + 1) - res > k:
                count[s[left]] -= 1
                left += 1
            
        return (r - left + 1)