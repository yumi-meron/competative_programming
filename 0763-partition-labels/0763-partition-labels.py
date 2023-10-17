class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        index_map = {}
        for x, element in enumerate(s):
            index_map[element] = x
        ans = []
        size, end = 0, 0
        for i, element in enumerate(s):
            size+=1
            end = max(end, index_map[element])
            
            if i==end:
                ans.append(size)
                size=0
        return ans
                
        