class Solution:
    def bestClosingTime(self, cust: str) -> int:
        pre = 0
        suff = cust.count('Y')
        ind = (len(cust)+1, float('inf'))
        for i in range(len(cust)+1):
            if (pre + suff) < ind[1]:
                ind = (i, pre+suff)
            if i< len(cust) and cust[i] == 'Y':
                suff -= 1
            else:
                pre += 1
        return ind[0] 

        