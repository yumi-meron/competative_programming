from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic1 = Counter(s1)
        n = len(s1)
        left = 0
        if n<2 and s1==s2 :
            return True
        for i in range(len(s2)-1):
            sub = s2[left:left+n]
            dic2 = Counter(sub)
            if dic1==dic2:
                return True
            left+=1
        return False
            
        