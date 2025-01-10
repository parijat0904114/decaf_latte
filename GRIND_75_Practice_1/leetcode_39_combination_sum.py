# class Solution(object):
#     def combinationSum(self, candidates, target):
#         """
#         :type candidates: List[int]
#         :type target: int
#         :rtype: List[List[int]]
#         """
#         result = []

#         def dfs(i, cur, total):
#             if total == target:
#                 result.append(list(cur))
#                 return
#             if total > target or i >= len(candidates):
#                 return
#             cur.append(candidates[i])
#             dfs(i, cur, total + candidates[i])
#             cur.pop()
#             dfs(i+1, cur, total)

#         dfs(0, [], 0)
#         return result


class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(i, cur, total):
            if total == 0:
                res.append(list(cur))
                return
            if total < 0 or i < 0:
                return
            cur.append(candidates[i])
            dfs(i, cur, total-candidates[i])
            cur.pop()
            dfs(i-1, cur, total)

        dfs(len(candidates)-1, [], target)
        return res


s = Solution()
print(s.combinationSum([2, 3, 4, 7], 4))
