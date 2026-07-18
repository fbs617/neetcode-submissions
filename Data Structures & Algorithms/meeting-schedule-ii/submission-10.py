"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.end)
        if len(intervals) == 0:
            return 0
        ends = [intervals[0].end]
        for i in range(1, len(intervals)):
            edited = False
            ends.sort(reverse=True)
            for j in range(len(ends)):
                if (intervals[i].start >= ends[j]):
                    ends[j] = intervals[i].end
                    edited = True
                    break
            if (edited == False):
                ends.append(intervals[i].end)
            print(ends)
        return len(ends)