class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        rows = len(grid)
        columns = len(grid[0])
        dir_map = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def dfs(row, col):
            grid[row][col] = '0'
            for dir_r, dir_c in dir_map:
                new_row, new_col = row + dir_r, col + dir_c
                if new_row >= 0 and new_col >= 0 and new_row < rows and new_col < columns and grid[new_row][new_col] == '1':
                    dfs(new_row, new_col)

        num_islands = 0

        for r in range(rows):
            for c in range(columns):
                if grid[r][c] == '1':
                    num_islands += 1
                    dfs(r, c)
        return num_islands


s = Solution()
print(s.numIslands([
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]))
print(s.numIslands([["1"], ["1"]]))
