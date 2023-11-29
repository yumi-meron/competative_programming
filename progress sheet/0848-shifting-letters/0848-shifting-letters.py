from itertools import accumulate
class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        shifts = reversed(list(accumulate(reversed(shifts))))
        for i, sh in enumerate(shifts):
                s[i] = chr(((ord(s[i])-ord('a')+sh)%26)+97)
        return ''.join(s)
        