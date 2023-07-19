class Solution:
    def makeSmallestPalindrome(self, s: str) -> str:
        i = 0
        j = len(s)-1
        s_lst = list(s)
        while i<j:
            if ord(s[i]) < ord(s[j]):
                s_lst[j] = s_lst[i]
            else:
                s_lst[i] = s_lst[j]
            i+=1
            j-=1
        return ''.join(s_lst)