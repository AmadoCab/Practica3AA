class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        def explore(r, c, count):
            if not (0 <= r < len(grid) and 0 <= c < len(grid[0]) and grid[r][c] == 1):
                return count
            grid[r][c] = 0
            count += 1
            count = explore(r-1, c, count)
            count = explore(r+1, c, count)
            count = explore(r, c-1, count)
            count = explore(r, c+1, count)
            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                max_area = max(explore(r,c,0), max_area)
        return max_area

# EOF #
