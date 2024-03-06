class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        def check(string):
            if not string:
                return ""
            sett = set(string)

            for i,char in enumerate(string):
                if char.swapcase() not in sett:
                    left = check(string[:i])
                    right = check(string[i+1:])
                    return max(left, right, key = len)
            return string
            
        return check(s)

        