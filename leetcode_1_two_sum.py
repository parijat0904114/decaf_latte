class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i, n in enumerate(nums):
            if target - n in num_dict:
                return [num_dict[target-n], i]
            num_dict[n] = i
s = Solution()
print(s.twoSum([3, 2, 4], 6))