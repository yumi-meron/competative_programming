class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        else:
            x = k - numOnes
            if x <= numZeros:
                return numOnes
            else:
                y = x - numZeros
                return numOnes - y
        
        