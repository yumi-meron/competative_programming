class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        right_boarder = len(board[0])
        lower_boarder = len(board)
        up_boarder = 0

        curr_letter = None
        seen = set()
        def backtrack(i,j,idx):
            if idx == len(word):
                return True
            if i < 0 or j < 0 or i >= lower_boarder or j >= right_boarder:
                return 
            if (i,j) in seen:
                return 
            if board[i][j] != word[idx]:
                return False
            seen.add((i,j))
            if backtrack(i,j+1, idx+1):
                return True

            if backtrack(i+1,j, idx+1):
                return True

            if backtrack(i-1,j, idx+1):
                return True

            if backtrack(i,j-1, idx+1):
                return True
                
            seen.remove((i,j))
            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if backtrack(i,j, 0):
                        return True
        return False
    