class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        i = 0
        returning_interval = []
        start, end = newInterval
        int_len = len(intervals) - 1

        # case 1: Adding intervals before the new interval
        while i <= int_len and intervals[i][1] < start:
            returning_interval.append(intervals[i])
            i += 1

        # case 2: merge overlapping intervals with new interval if applicable
        while i <= int_len and intervals[i][0] <= end:
            start = min(start, intervals[i][0])
            end = max(end, intervals[i][1])
            i += 1
        # case 3: directly add the new interval if there is no overlapping
        returning_interval.append([start, end])

        # case 4: add the remaining intervals afterwards
        while i <= int_len:
            returning_interval.append(intervals[i])
            i += 1

        return returning_interval


s = Solution()
print(s.insert([[1, 3], [6, 9]], [2, 5]))
