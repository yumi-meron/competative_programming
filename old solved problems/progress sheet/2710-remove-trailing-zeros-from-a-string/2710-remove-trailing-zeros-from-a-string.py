class Solution(object):
    def removeTrailingZeros(self, num):
        """
        :type num: str
        :rtype: str
        """
        l = len(num)-1
        while l >= 0 and num[l]== '0':
    
            l-=1
        return num[:l+1]
                
        