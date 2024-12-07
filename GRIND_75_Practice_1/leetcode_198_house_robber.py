class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s_1, s_2 = 0

        for num in nums:
            tmp = max(num + s_1, s_2)
            s_1 = s_2
            s_2 = tmp
        return s_2


s = Solution()
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([1, 2, 3, 1]))
