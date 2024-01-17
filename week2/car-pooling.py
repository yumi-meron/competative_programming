class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        pre = [0] * (1000+2)
        for trip in trips:
            ppl, start, end = trip
            pre[start] += ppl
            pre[end ] -= ppl
        for i in range(1,len(pre)):
            pre[i] += pre[i-1]
        return all([x <= capacity for x in pre])

        