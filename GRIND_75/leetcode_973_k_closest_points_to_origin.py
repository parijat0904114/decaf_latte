# Optimal Solution
# Lambda Sorting along with Slicing
class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        # Always use .sort() instead of sorted().
        # .sort() does in place sorting.
        points.sort(key=lambda x: x[0]**2 + x[1]**2)
        # We could return [:k]. However it would cost us
        # some space complexity. To reduce it from O(k) to O(1)
        # the following while loop is used.
        while k != len(points):
            points.pop()
        return points


s = Solution()
print(s.kClosest([[3, 3], [5, -1], [-2, 4]], 2))
