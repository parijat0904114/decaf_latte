class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if image[sr][sc] == color:
            return image
        prev_color = image[sr][sc]
        row = len(image)
        col = len(image[0])

        def DFS(sr, sc):
            if (0 <= sr < row and 0 <= sc < col and image[sr][sc] == prev_color):
                image[sr][sc] = color
                DFS(sr + 1, sc)
                DFS(sr, sc + 1)
                DFS(sr - 1, sc)
                DFS(sr, sc - 1)
            return image
        return DFS(sr, sc)


s = Solution()
print(s.floodFill(([1, 1, 1], [1, 1, 0], [1, 0, 1]), 1, 1, 2))
