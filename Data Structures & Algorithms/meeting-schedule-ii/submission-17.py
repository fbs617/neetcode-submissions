"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        starts = []
        ends = []
        for i in intervals:
            starts.append(i.start)
            ends.append(i.end)
        starts.sort()
        ends.sort()
        s = 0
        e = 0
        count = 0
        max_count = 0
        while (s < len(starts)):
            if (starts[s] < ends[e]):
                s += 1
                count += 1
                print("count: ", count)
            else:
                e += 1
                max_count = max(max_count, count)
                count -= 1
            if (s == len(starts)):
                max_count = max(max_count, count)
                print("max: ", max_count)
        return max_count












        # intervals.sort(key=lambda x: x.end)
        # if len(intervals) == 0:
        #     return 0
        # ends = [intervals[0].end]
        # for i in range(1, len(intervals)):
        #     edited = False
        #     ends.sort(reverse=True)
        #     for j in range(len(ends)):
        #         if (intervals[i].start >= ends[j]):
        #             ends[j] = intervals[i].end
        #             edited = True
        #             break
        #     if (edited == False):
        #         ends.append(intervals[i].end)

        # return len(ends)