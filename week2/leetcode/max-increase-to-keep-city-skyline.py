class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        rowmax = [0] * n
        colmax = [0] * m
        for i in range(n):
            for j in range(m):
                rowmax[i] = max(rowmax[i], grid[i][j])
                colmax[j] = max(colmax[j], grid[i][j])
        ans = 0
        for i in range(n):
            for j in range(m):
                x = min(rowmax[i], colmax[j])
                ans += x - grid[i][j]
        return ans
