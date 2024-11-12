"""
Definition of Interval:
"""


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution:
    def canAttendMeetings(self, intervals):
        length = len(intervals)
        if length == 0:
            return True

        low = intervals[0].start
        high = intervals[0].end
        for i in range(1, length):
            if intervals[i].start >= low and intervals[i].end <= high:
                return False
            low = max(low, intervals[i].start)
            high = min(high, intervals[i].end)

        return True


s = Solution()
i1 = Interval(0, 30)
i2 = Interval(5, 10)
i3 = Interval(15, 20)
i4 = Interval(1, 5)
i5 = Interval(1, 3)
print(s.canAttendMeetings([i1, i2, i3]))
print(s.canAttendMeetings([i4, i5]))
