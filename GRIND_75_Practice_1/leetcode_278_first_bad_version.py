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
        low = 0
        high = n

        while(low<high):
            mid = low + (high - low) // 2
            if isBadVersion(mid):
                high = mid
            else:
                low = mid + 1
        return low

# Returning either `low` or `high` is sufficient to display the
# correct answer. However, returning `mid` wouldn't work.
# As you can see, we increase the value of `low` by adding one
# to the value of `mid`. So if a calculated `mid` value is 3,
# `low` would have the value 4, and that might be where `low`
# converges with `high`.
