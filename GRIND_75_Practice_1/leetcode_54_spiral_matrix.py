class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        r = len(matrix) - 1
        c = len(matrix[0]) - 1
        l, u = 0, 0
        res = []

        while l <= r and u <= c:
            i, j = l, u

            while j < c:
                res.append(matrix[i][j])
                j += 1

            while i < r:
                res.append(matrix[i][j])
                i += 1

            while u < j:
                res.append(matrix[i][j])
                j -= 1

            while l < i:
                res.append(matrix[i][j])
                i -= 1
            l += 1
            r -= 1
            u += 1
            c -= 1
        return res


s = Solution()
print(s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))
print(s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
