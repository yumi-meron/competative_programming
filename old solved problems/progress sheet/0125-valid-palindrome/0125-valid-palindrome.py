class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        string = "".join(c for c in s if c.isalnum()).lower() 
        i,j=0,len(string)-1
        while i<j:
            if string[i]!=string[j]:
                return False
            i+=1
            j-=1
        else:
            return True
                
        