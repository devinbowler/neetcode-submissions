class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key=lambda x: x[0])
        index = 0
        returnVal = 0

        for interval in intervals:
            if not res or res[-1][1] <= interval[0]:
                res.append(interval)
            else:
                if res[-1][1] > interval[1]:
                    res[-1] = interval
                returnVal += 1

        return returnVal