from collections import deque


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        n_row = len(mat)
        n_col = len(mat[0])
        queue = deque()

        for i in range(n_row):
            for j in range(n_col):
                if mat[i][j] != 0:
                    mat[i][j] = float('inf')
                else:
                    queue.append([i, j])
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        while queue:
            r, c = queue.popleft()
            for dir_r, dir_c in dir:
                new_dr, new_dc = r + dir_r, c + dir_c
                if (0 <= new_dr < n_row and 0 <= new_dc < n_col and
                        mat[new_dr][new_dc] > mat[r][c]+1):
                    mat[new_dr][new_dc] = mat[r][c] + 1
                    queue.append([new_dr, new_dc])
        return mat


s = Solution()
print(s.updateMatrix([[0, 0, 0], [0, 1, 0], [1, 1, 1]]))
