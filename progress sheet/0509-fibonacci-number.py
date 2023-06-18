class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        fi = 0
        if n < 2:
            return n
        else:
            x = 0
            y = 1
            for i in range(n-1):
                fi = x + y
                x = y
                y = fi
            return fi
            
        