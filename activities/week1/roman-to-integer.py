class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        ans = 0
        for i in range(len(s)):
            if i!=0 and dic[s[i]]>dic[s[i-1]]:
                ans += abs(dic[s[i]]- 2*dic[s[i-1]])
            else:
                ans += dic[s[i]]
          
        return ans


        