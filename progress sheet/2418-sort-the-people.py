class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(1,len(heights)):
            j = i
            while j>0 and heights[j-1]<heights[j]:
                heights[j-1], heights[j] = heights[j], heights[j-1]
                names[j-1], names[j] = names[j], names[j-1]
                j-=1
        return names
        
            
                
            
        