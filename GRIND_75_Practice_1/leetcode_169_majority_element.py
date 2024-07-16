import math

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = sorted(nums)
        count = 1
        majority_element = nums[0]
        for i in nums[1:]:
            if i == majority_element:
                count += 1
            else:
                if count > math.floor(len(nums) // 2):
                    return majority_element
                else:
                    count = 1
                    majority_element = i
        return majority_element

s = Solution()
print(s.majorityElement([2,2,1,1,1,2,2]))