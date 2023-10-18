from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        dic = Counter(p)
        k = len(p)
        left = 0
        ans = []
        for i in range(len(s)-k+1):
            now = Counter(s[left:left+k])
            if dic == now:
                ans.append(left)
            left+=1
        return ans
        