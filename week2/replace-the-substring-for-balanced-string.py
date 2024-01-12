class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)//4
        left, ans, count = 0,float('inf'), Counter(list(s))

        for key in list(count.keys()):
            if count[key] <= n:
                del count[key]
            else:
                count[key] -= n
        
        for right in range(len(s)):
            if s[right] in count:
                count[s[right]] -= 1
            while all(value <= 0 for value in count.values()):
                if left == len(s):
                    break
                if  s[left] in count:
                    count[s[left]] += 1
                ans = min(ans, right - left + 1)
                left += 1
               
        return ans if (ans != float('inf') and ans > 0) else 0
        


        


        return ans
        