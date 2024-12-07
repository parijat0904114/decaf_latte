class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def backtrack(path, used):
            if len(path) == len(nums):
                res.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                path.append(nums[i])
                used[i] = True

                backtrack(path, used)

                path.pop()
                used[i] = False

        res = []
        used = [False] * len(nums)
        backtrack([], used)
        return res


s = Solution()
print(s.permute([1, 2, 3]))
