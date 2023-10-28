class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        s = list(s)
        prefix = [0]*len(s)
        for shift in shifts:
            start, end, dxn = shift
            prefix[start] += dxn if dxn == 1 else -1
            if end+1<len(prefix):
                prefix[end+1] -= dxn if dxn==1 else -1
            
        for i in range(1,len(prefix)):
            prefix[i]+= prefix[i-1]
        for i, sh in enumerate(prefix):
            s[i] = chr(((ord(s[i])-ord('a')+sh)%26)+97)
        return ''.join(s)
            
            