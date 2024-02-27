class Solution:
    def __init__(self):
        self.reverse = 0
    def kthGrammar(self, n: int, k: int) -> int:
        
        def func(n,k):
            if n == 1:
                return self.reverse

            half = pow(2, (n-1)) // 2
            if k > half: 
                self.reverse += 1
                k -= half 
        
            return func(n-1,k)
        func(n,k)
        if self.reverse % 2:
            return 1
        else:
            return 0



        

        


        