class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        points.sort(key = lambda p:p[0])
        max_width = 0
        for i in range(1,len(points)):
            diff = points[i][0] - points[i-1][0]
            if diff>max_width:
                max_width = diff
        return max_width
        