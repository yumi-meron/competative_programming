class Solution:
    def splitString(self, s: str) -> bool:
        values = []
        def backtrack(idx):
            if idx >= len(s):
                return len(values) >= 2
            
            for i in range(idx,len(s)):
                curr = s[idx:i+1]
                if not values or values[-1] - int(curr) == 1:
                    values.append(int(curr))
                    if backtrack(i+1):
                        return True
                    values.pop()
        return backtrack(0)
                

                

        