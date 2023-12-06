class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = ''.join(c for c in s if c.isalnum())
        print(s)
        a=0
        b = len(s)-1
        while a<b:
            if s[a]!=s[b]:
                return False
            a+=1
            b-=1
        else:
            return True
        