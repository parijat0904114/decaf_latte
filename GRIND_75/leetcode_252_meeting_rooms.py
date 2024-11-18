
# Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end


class Solution (object):
    def canAttendMeetings(self, intervals):
        """
        :type intervals: Interval
        :rtype: bool
        """
        intervals.sort(key=lambda i: i.start)
        for i in range(1, len(intervals)):
            if intervals[i-1].end > intervals[i].start:
                return False
        return True


i1 = Interval(0, 30)
i2 = Interval(5, 10)
i3 = Interval(15, 20)

s = Solution()
print(s.canAttendMeetings([i1, i2, i3]))
print(s.canAttendMeetings([]))
