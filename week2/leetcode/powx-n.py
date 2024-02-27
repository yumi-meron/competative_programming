class Solution:
    def myPow(self, x: float, n: int) -> float:

        def power(n):
            if x == 0:
                return 0
            if n == 0:
                return 1
            
            half = power(n//2)
            half = half * half

            if n % 2 == 0:
                return half 
            else:
                return x * (half)

        ans = power(abs(n))

        return ans if n > 0 else 1 / ans
        
                
       
        