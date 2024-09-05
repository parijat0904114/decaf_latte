from collections import deque
class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        # Prepopulate with 
        # 0 -> 0 and
        # 1 -> inf weights
        queue = deque()
        rows = len(mat)
        columns = len(mat[0])

        for r in range(rows):
            for c in range(columns):
                if mat[r][c] == 0:
                    queue.append((r,c))
                else:
                    mat[r][c] = float('inf')

        # BFS
        direction_map = [(-1,0), (1,0), (0, 1), (0, -1)]
        while queue:
            r, c = queue.popleft()

            for dr, dc in direction_map:
                new_dr = r + dr
                new_dc = c + dc
                if 0<=new_dr<rows and 0<=new_dc<columns:
                    if mat[new_dr][new_dc] > mat[r][c] + 1:
                        mat[new_dr][new_dc] = mat[r][c] + 1
                        queue.append((new_dr, new_dc))
        return mat

s = Solution()
print(s.updateMatrix([[0,0,0],[0,1,0],[1,1,1]]))
        