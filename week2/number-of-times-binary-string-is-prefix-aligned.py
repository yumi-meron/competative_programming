class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        summ = 0
        count = 0
        temp = [0 for i in range(len(flips))]
        for i in range(len(flips)):
            temp[flips[i]-1] = 1
            summ += temp[i]
            if flips[i] < i+1:
                summ += 1
            if summ == i+1 :
                count += 1           
                
        return count 

        