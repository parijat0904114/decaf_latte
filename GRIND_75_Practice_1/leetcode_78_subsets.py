class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        subsets = [[]]

        for num in nums:
            new_subsets = []
            for subset in subsets:
                new_subsets += [subset + [num]]
            subsets.extend(new_subsets)
        return subsets


s = Solution()
print(s.subsets([1, 2, 3]))
