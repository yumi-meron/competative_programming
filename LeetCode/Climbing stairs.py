class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0 or n==1 or n==2:
            return n
        else:
            x = 1
            y = 2
            for i in range(2, n):
                ai = x + y
                x = y
                y = ai
                
        return ai
