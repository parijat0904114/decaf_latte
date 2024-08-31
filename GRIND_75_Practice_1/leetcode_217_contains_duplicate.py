# class Solution(object):
#     def containsDuplicate(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: bool
#         """
#         return len(nums) != len(set(nums))


class Solution(object):
    def containsDuplicate(self, nums):
        hash_set = set()
        for num in nums:
            if num in hash_set:
                return True
            hash_set.add(num)
        return False

s = Solution()
print(s.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
print(s.containsDuplicate([1,2,3,4]))