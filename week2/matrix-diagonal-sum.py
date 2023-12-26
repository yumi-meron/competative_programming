class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        summ = 0
        i,j = 0,0
        while i<n and j<n:
            summ += mat[i][j]
            i+=1
            j+=1
        
        i,j = 0,n-1
        while i<n and j>=0:
            summ += mat[i][j]
            i+=1
            j-=1
        if n % 2:
            summ -= mat[n//2][n//2]
        return summ
        
        

        