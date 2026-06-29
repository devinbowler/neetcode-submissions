class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        res = []
        intervals.sort(key=lambda x: (x[0], -x[1]))
        print(intervals)
        returnVal = 0

        for interval in intervals:
            # If res is empty or the current interval does not overlap
            if not res or res[-1][1] <= interval[0]:
                res.append(interval)
            else:
                # Overlap detected: Increment the count and remove the interval with the larger end time
                if res[-1][1] > interval[1]:
                    res[-1] = interval  # Replace with the interval that has a smaller end
                returnVal += 1

        return returnVal