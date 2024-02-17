class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        arrows = 1
        lastL = points[0]
        for point in points:
            if point[0] > lastL[1]:
                arrows += 1
                lastL = point
        return arrows

        