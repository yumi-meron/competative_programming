class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(s1)
        left, right = 0,len(s1)
        while right <= len(s2):
            sub = sorted(s2[left:right])
            right += 1
            left += 1
            if sub == s1:
                return True
        return False
        