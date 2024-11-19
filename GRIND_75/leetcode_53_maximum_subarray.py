# Trivial Solution
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum, n = nums[0], len(nums)
        for i in range(n):
            cur = 0
            for j in range(i, n):
                cur += nums[j]
                max_sum = max(cur, max_sum)
        return max_sum

# Optimized Solution


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
