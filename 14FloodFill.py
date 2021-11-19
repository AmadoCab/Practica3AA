class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        target = image[sr][sc]
        def dfs(image, r, c, target, newColor):
            image[r][c] = newColor
            if r > 0:
                if image[r-1][c] == target:
                    dfs(image, r-1,c, target, newColor)
            if c > 0:
                if image[r][c-1] == target:
                    dfs(image, r,c-1, target, newColor)
            if r < len(image)-1:
                if image[r+1][c] == target:
                    dfs(image, r+1,c, target, newColor)
            if c < len(image[0])-1:
                if image[r][c+1] == target:
                    dfs(image, r,c+1, target, newColor)
            return image

        if target == newColor:
            return image
        return dfs(image, sr, sc, target, newColor)

# EOF #
