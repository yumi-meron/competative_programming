class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s=list(s)
        pre = [0] * (len(s)+1)
        for shift in shifts:
            start, end, dxn = shift
            pre[start] += 1 if dxn == 1 else -1
            if end + 1 < len(pre): 
                pre[end + 1] -= 1 if dxn == 1 else -1
                
            
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        for idx,char in enumerate(s):
            x = ord(char)
            x += pre[idx]
            y=(x-96)%26 or 26
            s[idx]=chr(y+96)
        return ''.join(s)




        