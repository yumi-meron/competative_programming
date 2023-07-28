class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left  = 0
        substring = set()
        result = 0
        for i in range(0,len(s)):
            while s[i] in substring:
                substring.remove(s[left])
                left+=1
            substring.add(s[i])
            result = max(result, i-left+1)
            
        return result
        
        
                
        