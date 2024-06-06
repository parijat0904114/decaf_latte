class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash_map = {}
        for i, n in enumerate(nums):
            if target-n in hash_map:
                return [i, hash_map[target-n]]
            hash_map[n] = i

# s = Solution()
# print(s.twoSum([2,7,11,15], 9))