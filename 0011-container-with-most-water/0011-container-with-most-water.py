class Solution:
    def maxArea(self, height: List[int]) -> int:
        most = 0
        i=0
        j= len(height)-1
        while i<j:
                diff = j-i
                h = min(height[i], height[j])
                most = max(most, diff * h)
                if height[i]<height[j]:
                    i+=1
                else:
                    j-=1
        return most
        
        