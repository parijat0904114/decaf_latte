class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        updated_mat = [[-1 for _ in range(len(mat[0]))]for _ in range(len(mat))]

        def dfs(i, j, depth):
            if mat[i, j] == 0:
                return updated_mat[i][j] = 1 + depth
            elif mat[]

        dfs(0,0,0)         
s = Solution()
s.updateMatrix([[0,0,0],[0,1,0],[0,0,0]])