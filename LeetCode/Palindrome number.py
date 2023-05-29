class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev_x = str(x)[::-1]
        if str(x)==rev_x:
            return True
        else:
            return False
