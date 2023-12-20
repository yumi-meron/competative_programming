class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ans = list(zip(*matrix))
        return ans

            
        