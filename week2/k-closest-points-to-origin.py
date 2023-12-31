class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def distance(l):
            return pow(l[0],2) + pow(l[1],2)
        points.sort(key = distance)
        return points[:k]
        