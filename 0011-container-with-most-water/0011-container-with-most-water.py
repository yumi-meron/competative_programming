class Solution:
    def maxArea(self, height: List[int]) -> int:
        i = 0
        j = len(height)-1
        most = 0
        while i<j:
            most = max(min(height[i],height[j]) * (j-i), most)
            if height[i]<height[j]:
                i+=1
            else:
                j-=1
        return most
            
        