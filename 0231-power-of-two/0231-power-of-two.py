class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        elif n<2:
            return False
        elif n%2 != 0:
            return False
        
        
    
        return self.isPowerOfTwo(n/2)