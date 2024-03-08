class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ends = [mat[-1] for mat in matrix]
        idx = bisect_left(ends, target)
        if idx >= len(matrix):
            return False
        else:
            col_idx = bisect_left(matrix[idx],target)
            if col_idx == 0 and matrix[idx][col_idx] != target:
                return False
            elif col_idx >= len(matrix[idx]):
                return False
            elif matrix[idx][col_idx] != target:
                return False
        return True
