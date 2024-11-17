class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        a = 1  # There is only one way to climb 1 step.
        b = 2  # There are two ways to climb 2 steps. 1 + 1, 2.
        for _ in range(3, n+1):
            a, b = b, a+b
        return b if n > 1 else a


s = Solution()
print(s.climbStairs(5))
