class Solution(object):
    def maxCoins(self, piles):
        """
        :type piles: List[int]
        :rtype: int
        """
        sum=0
        piles.sort()
        pile=[x for x in piles[len(piles)/3:]]
        for i in range(len(pile)):
            if i%2==0:
                sum += pile[i]
       
        return sum
                
            
        