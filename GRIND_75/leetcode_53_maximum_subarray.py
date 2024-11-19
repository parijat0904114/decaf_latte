class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_l, max_g = nums[0], nums[0]
        for i in range(1, len(nums)):
            local_sum = max_l + nums[i]
            max_l = nums[i] if nums[i] > local_sum else local_sum
            max_g = max(max_l, max_g)
        return max_g


s = Solution()
print(s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
