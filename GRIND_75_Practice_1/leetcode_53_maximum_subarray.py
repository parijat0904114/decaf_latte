class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_local = max_global = nums[0]
        for i in range(1, len(nums)):
            max_local = max_local + nums[i] if max_local + nums[i] > nums[i] else nums[i]
            max_global = max_local if max_local > max_global else max_global
        return max_global
        
s = Solution()
print(s.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))