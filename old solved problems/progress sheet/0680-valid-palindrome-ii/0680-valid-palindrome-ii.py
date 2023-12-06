from collections import Counter
class Solution:              
    def validPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s)-1
        while i<j:
            if s[i] != s[j]:
                skipi = s[i+1:j+1]
                skipj =s[i:j]
                if (skipi == skipi[::-1] or skipj == skipj[::-1]):
                    return True
                else:
                    return False
            i+=1
            j-=1
        return True
                
                
                    
                
                
        
            
            
        
         
        