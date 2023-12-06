class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        ans = 0
        for i in range(len(points)-1):
            #finding the amount of steps it takes from on point to the other
            x_axis = abs(points[i][0]-points[i+1][0])
            y_axis = abs(points[i][1]-points[i+1][1])
            #taking the maximum step and adding it to our answer
            ans += max(x_axis,y_axis)
        return ans
        

        