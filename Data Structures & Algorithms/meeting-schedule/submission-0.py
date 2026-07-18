"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key=lambda x:x.start)
        i = 0
        j = 1
        while (j < len(intervals)):
            if intervals[i].end > intervals[i+1].start:
                return False
            elif intervals[i].end > intervals[j].end:
                j += 1
            else:
                i += 1
                j += 1
        return True

                


