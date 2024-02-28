class Solution:
    def countGoodNumbers(self, n: int) -> int:
        MOD = (pow(10, 9) + 7)
        if n % 2:

            return pow(4, (n//2), MOD) * pow(5, (n//2 + 1), MOD) % MOD
        else:
            return pow(4, (n//2), MOD) * pow(5, (n//2), MOD) % MOD
        
        
        
        