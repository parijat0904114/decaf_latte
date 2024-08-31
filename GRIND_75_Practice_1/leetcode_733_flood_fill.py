class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        if not image or image[sr][sc]==color:
            return image
        previous_color = image[sr][sc]
    
        def dfs(sr, sc):
            if (sr<0 or sc<0 or
                sr>=len(image) or
                sc>=len(image[0]) or
                image[sr][sc]!=previous_color):
                return
            image[sr][sc] = color
            dfs(sr + 1, sc)
            dfs(sr - 1, sc)
            dfs(sr, sc + 1)
            dfs(sr, sc - 1)
        dfs(sr, sc)
        return image

s = Solution()
print(s.floodFill([[1,1,1],[1,1,0],[1,0,1]], 1, 1, 2))

