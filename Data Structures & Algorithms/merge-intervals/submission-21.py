class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort intervals by start value
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        res = []
        
        for interval in intervals:
            # If res is empty or the current interval does not overlap with the last one
            if not res or res[-1][1] < interval[0]:
                res.append(interval)
            else:
                # Overlapping intervals: merge them
                res[-1][1] = max(res[-1][1], interval[1])
        
        return res