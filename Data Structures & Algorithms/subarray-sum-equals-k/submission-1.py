class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curSum = 0
        indexTable = { 0 : 1}

        for n in nums:
            curSum += n
            diff = curSum - k

            res += indexTable.get(diff, 0)
            indexTable[curSum] = 1 + indexTable.get(curSum, 0)

        return res

