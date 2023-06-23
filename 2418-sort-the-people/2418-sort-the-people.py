class Solution(object):
    def sortPeople(self, names, heights):
        """
        :type names: List[str]
        :type heights: List[int]
        :rtype: List[str]
        """
        for i in range(len(heights)):
            max = heights[i]
            pos = i
            for j in range(i+1,len(heights)):
                if heights[j] > max:
                    max = heights[j]
                    pos = j
            heights[i], heights[pos] = heights[pos], heights[i]
            names[i], names[pos] = names[pos], names[i]
            
        return names
        
            
                
            
        