class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        myset = {'a','e','o','i','u'}
        left,count,ans =0,0, 0
        for right in range(len(s)):
            if s[right] in myset:
                count += 1
            if right - left >= k:
                if s[left] in myset:
                    count -= 1
                
                left += 1
            ans = max(ans, count)

                
        return ans

            
        