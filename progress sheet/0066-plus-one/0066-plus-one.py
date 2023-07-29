class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        carry = 0
        n = len(digits)
        for i in reversed(range(n)):
            if i == n-1:
                value = digits[i] + 1
            else:
                value = digits[i] + carry
            if value <= 9:
                digits[i] = value
                carry = 0
            else:
                carry = value//10
                value -= 10
                digits[i] = value
        if carry:
            digits.insert(0,carry)
        return digits
        
     

        
             