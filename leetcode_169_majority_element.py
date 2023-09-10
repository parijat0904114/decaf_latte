class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) // 2]


# obj = Solution()
# print(obj.majorityElement([2, 2, 1, 1, 1, 2, 2]))
