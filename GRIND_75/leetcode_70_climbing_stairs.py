class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1
        b = 2
        while (n >= 2):
            a, b = b, a+b
            n -= 1
        return a


s = Solution()
print(s.climbStairs(5))
