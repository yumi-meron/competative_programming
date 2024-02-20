class Solution:
    def breakPalindrome(self, pali: str) -> str:
        N = len(pali) #length of our string

        if len(pali) <= 1:
            return ""

        pal = list(pali)
        x = 0
        if N%2: x = 1 #if length of our string is odd changes made at the middle element will not make our string non palidrome

        #since the least lexicographical letter is a we try to change any letter d/t from 'a' to 'a'
        for i,char in enumerate(pal):
            #if we are the last index and still haven't found a letter d/t from 'a' we change the last letter to 'b'
            if i == N-1 and char == 'a':
                pal[i] = 'b'
            
            elif char != 'a':
                #by checking it's not the middle element we change it to 'a'
                if x==1:
                    if (N//2) != i:
                        pal[i] = 'a'
                        break
                elif x == 0:
                    
                    pal[i] = 'a'
                    break
            
        return ''.join(pal) if ''.join(pal) != pali else ""

