class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        mp = {}
        for i,char in enumerate(s) :
            mp[char] = i
        last = mp[s[0]]
        left = 0
        ans = []
        for i,char in enumerate(s):
            if mp[char] > last:
                last = mp[char]
            if i == last: 
                ans.append(last - left + 1)
                left = last + 1
                
            
        
        return ans

        