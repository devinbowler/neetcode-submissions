class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(index, arr, curSum):
            if curSum == target:
                tempArr = sorted(arr.copy())
                if tempArr not in res:
                    res.append(sorted(arr.copy()))
                return

            if index >= len(candidates) or curSum > target:
                return

            curVal = candidates[index]
            arr.append(curVal)
            dfs(index + 1, arr, curSum + curVal)
            arr.pop()
            dfs(index + 1, arr, curSum)

        dfs(0, [], 0)

        return res