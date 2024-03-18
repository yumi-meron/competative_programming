class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        def backtrack(string, l,r):
            if len(string) == 2*n:
                ans.append(string)
                return
            if l < n:
                backtrack(string + '(', l+1, r)
            if r < l:
                backtrack(string + ')', l, r+1)
        backtrack("", 0, 0)
        return ans

        