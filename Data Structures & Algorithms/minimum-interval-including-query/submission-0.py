class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        # we want to go through queries and check against the intervals if it would belong
        # to one. If it does not add -1 to a list, otherwise take the difference of intervals + 1 and add it.

        output = []

        for each in queries:
            compare = []
            for idx, (low, high) in enumerate(intervals):
                if low <= each <= high:
                    compare.append((high - low) + 1)
                
                if idx == len(intervals) - 1 and len(compare) == 0:
                    output.append(-1)
                elif idx == len(intervals) - 1:
                    output.append(min(compare))
                

        return output