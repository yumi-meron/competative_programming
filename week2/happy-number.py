class Solution:
    def isHappy(self, n: int) -> bool:
        i = 0
        while n > 1 and i<10:
            temp = list(map(int,str(n)))
            n = sum(num**2 for num in temp)
            i+=1


            
        return n == 1

            
            
        
        