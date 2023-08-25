# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        mid = 0
        while low < high:
            mid = (
                low + (high - low) // 2
            )  # nice way to determine average by avoiding integer overflow
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high  # returning low would also work. in the end low and high would converge to the same point.
