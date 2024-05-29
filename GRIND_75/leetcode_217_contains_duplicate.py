# Better Time Complexity
class Solution(object): 
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        s = set()
        for num in nums:
            if num in s:
                return True
            s.add(num)
        return False

# Better Space Complexity    
class Solution2(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # Taking advantage of not using any extra space
        # by Sorting.
        nums = sorted(nums)
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True
        return False

# s = Solution()
# print(s.containsDuplicate([1, 2, 3, 1]))

# s = Solution2()
# print(s.containsDuplicate([3,4,1,4,5,2]))