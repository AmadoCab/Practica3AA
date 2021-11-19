class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        for i in range(len(triangle)-1):
            for j in range(len(triangle[i+1])):
                if j == 0:
                    triangle[i+1][j] += triangle[i][j]
                elif j == len(triangle[i]):
                    triangle[i+1][j] += triangle[i][j-1]
                else:
                    triangle[i+1][j] += min(triangle[i][j],triangle[i][j-1])
        return min(triangle[-1])

# EOF #
