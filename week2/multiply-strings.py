class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        #initializing a space where we store our product
        product = [0] * (len(num1) + len(num2))
        pos = len(product)-1 

        #by itrating over both nums in reversed order do basic multiplication
        for n1 in reversed(num1):
            temp_pos = pos
            for n2 in reversed(num2):
                #first finding the product
                product[temp_pos] += int(n1) * int(n2)
                #storing the carry on the index before current pos
                product[temp_pos-1] += product[temp_pos] // 10 
                #storing the ones place on our current position
                product[temp_pos] %= 10
                temp_pos -= 1  #decrement our position
            pos -= 1 

        # finding the start position where the leading zeros end
        start = 0
        while start < len(product)-1 and product[start] == 0:
            start += 1

        #return ans as a string
        return ''.join(map(str, product[start:]))   
        