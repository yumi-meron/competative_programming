class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        l = 0
        score = 0
        for i in range(len(s)):
            if s[i] == '(':
                l +=1
            else:
                l-=1
                if s[i-1] == '(':
                    score += 2**(l)
        return score