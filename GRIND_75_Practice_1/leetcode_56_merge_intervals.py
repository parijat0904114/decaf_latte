class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        new_intervals = [intervals[0]]

        for i in range(1, len(intervals)):

            if intervals[i][0] <= new_intervals[-1][1]:
                new_intervals[-1][1] = max(intervals[i][1],
                                           new_intervals[-1][1])
            else:
                new_intervals.append(intervals[i])

        return new_intervals


s = Solution()
print(s.merge([[1, 3], [2, 6], [8, 10], [15, 18]]))
