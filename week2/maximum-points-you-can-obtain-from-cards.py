class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        
        left = 0
        pre = sum (cardPoints)
        runsum = sum(cardPoints[:n-k])
        ans = pre - runsum

        for right in range(n-k,n):
            runsum += cardPoints[right]
            runsum -= cardPoints[left]
            ans = max(ans, pre-runsum)
            left += 1
        
        return ans



            

        