class Solution:
    def largestOddNumber(self, num: str) -> str:
        #checking if the least significant digits are odd, cause that means the number is odd
        for i in range(len(num)-1,-1,-1):
            if int(num[i]) % 2:
                return num[:i+1]
        return ""

