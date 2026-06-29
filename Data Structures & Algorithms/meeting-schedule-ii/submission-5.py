class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __repr__(self):  # Clean representation for printing
        return f"({self.start}, {self.end})"


class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        dayMeetings = {}
        curDay = []
        intervals.sort(key=lambda x: x.start)
        print(intervals)

        if len(intervals) == 0:
            return 0

        def checkDict(index, interval, dic):
            if index in dayMeetings:
                if interval.start >= dic[index][-1].end:
                    dic[index].append(interval)
                else:
                    checkDict(index + 1, interval, dic)
            else:
                dic[index] = [interval]

        for interval in intervals:
            if not curDay or interval.start >= curDay[-1].end:
                curDay.append(interval)
            else:
                checkDict(0, interval, dayMeetings)
        
        print(curDay)
        for key, value in dayMeetings.items():
            print(f"Key: {key}, Value: {value}")
        return len(dayMeetings) + 1