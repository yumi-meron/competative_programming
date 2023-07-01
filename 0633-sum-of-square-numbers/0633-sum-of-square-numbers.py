class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        for a in range(int(c**0.5)+1):
            b = c - a**2
            if int(b**0.5) == b**0.5:
                return True
        return False
        
        