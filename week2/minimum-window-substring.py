class Solution:
    def minWindow(self, s: str, t: str) -> str:
        c1 = Counter(list(t))
        less = len(c1)
        left = 0
        ans = ""
        idxs = ()
        length = float('inf')

        for right, char in enumerate(s):
            if char in c1:
                c1[char] -= 1
                if c1[char] == 0: less -= 1

            while less < 1:
                if s[left] in c1: 
                    c1[s[left]] += 1
                    if c1[s[left]] > 0:less += 1
                if (right - left + 1) < length:
                    idxs = (left, right)
                    length = right - left + 1
                left += 1
        return s[idxs[0]: idxs[1]+1] if idxs else "" 
            


        