class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        root = sqrt(x)
        return int(math.floor(root))
