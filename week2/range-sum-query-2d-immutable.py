class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.matrix = matrix
        self.prefix = [[0]*(m+1) for _ in range(n+1)]
        for i in range(n):
            for j in range(m):
                self.prefix[i][j] = self.matrix[i][j] + self.prefix[i-1][j] + self.prefix[i][j-1] -  self.prefix[i-1][j-1]
                
               

        

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = self.prefix[row2][col2] - self.prefix[row1-1][col2] - self.prefix[row2][col1-1] + self.prefix[row1-1][col1-1]

        return ans
        
        


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)