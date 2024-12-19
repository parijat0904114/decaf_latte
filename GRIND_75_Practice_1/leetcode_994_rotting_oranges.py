from collections import deque


class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        q = deque()
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        time = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r, c))

        while fresh > 0 and q:
            length = len(q)
            while length > 0:
                row, col = q.popleft()
                dir_map = [(-1, 0), (1, 0), (0, 1), (0, -1)]
                for dir_r, dir_c in dir_map:
                    new_r, new_c = row + dir_r, col + dir_c
                    if rows > new_r >= 0 and cols > new_c >= 0 and grid[new_r][new_c] == 1:
                        fresh -= 1
                        grid[new_r][new_c] = 2
                        q.append((new_r, new_c))
                        print(q)
                length -= 1
            time += 1

        return time if fresh == 0 else -1


s = Solution()
print(s.orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]))
