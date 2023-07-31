class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        result = 0
        for i in accounts:
            maxi = sum(i)
            result = max(result, maxi)
        return result
            
        