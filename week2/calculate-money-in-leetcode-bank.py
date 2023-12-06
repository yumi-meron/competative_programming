class Solution:
    def totalMoney(self, n: int) -> int:
        summ = 0
        birr = 1
    
        for i in range(n):
            if i != 0 and i % 7 == 0:
                birr -= 6
            summ += birr
            birr += 1
        
        return summ

        