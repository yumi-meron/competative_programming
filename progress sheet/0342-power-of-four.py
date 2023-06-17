class Solution(object):
    def isPowerOfFour(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<=0:
            return False
        else:
            log_n = math.log(n, 4)
        return log_n.is_integer()
        