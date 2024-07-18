class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        returning_interval = []
        i = 0
        start, end = newInterval
        while i < len(intervals) and intervals[i][1] < start:
            returning_interval.append(intervals[i])
            i += 1

        while i < len(intervals) and intervals[i][0] <= end:
            start = min(intervals[i][0], start)
            end = max(intervals[i][1], end)
            i += 1

        returning_interval.append([start, end])

        while i < len(intervals):
            returning_interval.append(intervals[i])
            i += 1

        return returning_interval            

s = Solution()
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))
print(s.insert([[1,3], [6,9]], [2,5]))