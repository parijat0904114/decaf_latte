class Solution(object):
    def __init__(self):
        self.res = {}

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2 or n == 1:  # For n == 2, there are two ways to climb: (1,1) or (2).
            return n
        if n in self.res:
            return self.res[n]  # memoization technique to avoid TLE
        self.res[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.res[n]


# s = Solution()
# print(s.climbStairs(45))
