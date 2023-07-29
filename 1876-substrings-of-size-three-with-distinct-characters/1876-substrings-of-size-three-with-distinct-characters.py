class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        setmap = set()
        left =0
        count = 0
        for i in range(len(s)):
            while s[i] in setmap or len(setmap)>=3:
                setmap.remove(s[left])
                left+=1
            
            setmap.add(s[i])
            if len(setmap) == 3:
                count+=1
        return count
        