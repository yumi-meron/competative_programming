class Solution:
    def minimumSteps(self, s: str) -> int:
        
        zeros,ones = 0, 0
        steps = ones
        for i in range(len(s)):
            if s[i] == "1":
                ones += 1
            else:
                steps += ones 
        return steps
        
            

        