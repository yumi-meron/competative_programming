import sys
class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = ''
        x = str(x)
        if x[0] == "-":
            y = x[::-1]
            rev = int(x[0]+ y[:-1])
        else:
            rev = int(x[::-1])

        int_reversed = int(rev)
        if int_reversed < -2**31 or int_reversed > 2**31 - 1:
            return 0
        else:
            return int_reversed 

            