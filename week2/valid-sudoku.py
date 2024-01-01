class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        myset = set()
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue
                else:
                    row = (i,val)
                    col = (val, j)
                    box = (i//3,j//3,val)
                    if row in myset or col in myset or box in myset:
                        return False
                    myset.add(row)
                    myset.add(col)
                    myset.add(box)
        return True