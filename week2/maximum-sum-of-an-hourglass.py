class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        ans = 0
        for row in range(len(grid)-2):
            for column in range(len(grid[0])-2):
                summ = grid[row][column] + grid[row][column + 1] + grid[row][column + 2] + grid[row + 1][column + 1] + grid[row + 2][column] + grid[row + 2][column + 1] + grid[row + 2][column + 2]

                ans = max(ans,summ)
        return ans

        