class Solution:
    def maxScore(self, s: str) -> int:
        zeros ,ones = 0,s.count('1')
        maxx = 0
        for i in range(len(s)-1):
            if s[i] == '0':
                zeros += 1
            else:
                ones -= 1
            maxx = max(maxx, zeros+ones)
        return maxx
        