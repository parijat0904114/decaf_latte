class Solution(object):
    def permute(self, nums):
        def backtrack(start):
            if start == len(nums):
                res.append(nums[:])
            else:
                for i in range(start, len(nums)):
                    nums[start], nums[i] = nums[i], nums[start]
                    backtrack(start + 1)
                    nums[start], nums[i] = nums[i], nums[start]

        res = []
        backtrack(0)
        return res


s = Solution()
print(s.permute([1, 2, 3]))
