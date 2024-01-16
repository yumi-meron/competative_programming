class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, mp,maxCount, ans = 0, {} ,0, 0
        for right in range(len(s)):
            mp[s[right]] = mp.get(s[right], 0) + 1
            maxCount = max(maxCount, mp[s[right]])
            if (right - left + 1) - maxCount > k:
                mp[s[left]] -= 1
                left += 1
            ans = max(ans,right - left + 1)
        return ans
                
            


            

       