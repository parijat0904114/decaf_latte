class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # climbing stairs is just another form of fibonacci
        # base case 1,2 and then 3,5,8,13,21...
        a = 1
        b = 1
        while (n > 0):
            a, b = b, a+b
            n -= 1
        return a


s = Solution()
print(s.climbStairs(5))
