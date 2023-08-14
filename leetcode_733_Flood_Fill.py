class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image:
            return image
        if image[sr][sc] == color:
            return image

        def dfs(sr, sc, old_color, color):
            if (
                sr < 0
                or sr >= len(image)
                or sc < 0
                or sc >= len(image[0])
                or image[sr][sc] != old_color
            ):
                return
            image[sr][sc] = color
            dfs(sr + 1, sc, old_color, color)
            dfs(sr, sc + 1, old_color, color)
            dfs(sr - 1, sc, old_color, color)
            dfs(sr, sc - 1, old_color, color)

        dfs(sr, sc, image[sr][sc], color)
        return image


s = Solution()
print(s.floodFill([[1, 1, 1], [1, 1, 0], [1, 0, 1]], 1, 1, 2))
