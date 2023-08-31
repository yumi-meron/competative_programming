class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        x = sorted([i[0] for i in points])
        return max(x[i+1]-x[i] for i in range(len(x)-1))