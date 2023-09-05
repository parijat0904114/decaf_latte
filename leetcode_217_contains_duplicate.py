class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        d = {}
        for num in nums:
            if num in d:
                return True
            d[num] = None
        return False


# s = Solution()
# print(s.containsDuplicate([1, 2, 3, 1]))
