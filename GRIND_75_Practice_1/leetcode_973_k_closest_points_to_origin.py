from collections import defaultdict

class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        return sorted(points, key=lambda p: p[0]*p[0] + p[1]*p[1])[:k]

s = Solution()
print(s.kClosest([[4,6], [0,1], [1,0], [2,3]], 2))