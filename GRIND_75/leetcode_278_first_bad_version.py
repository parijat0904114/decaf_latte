class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        low = 1
        high = n
        while low < high:
            mid = low + (high - low)//2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return high  # or we can return low as well
