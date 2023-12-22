class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_local = max_global = nums[0]
        # remember range stops at len(nums) - 1 index.
        for i in range(1, len(nums)):
            max_local = max(nums[i], max_local + nums[i])
            max_global = max(max_global, max_local)
        return max_global


# obj = Solution()
# result = obj.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
# print(result)
