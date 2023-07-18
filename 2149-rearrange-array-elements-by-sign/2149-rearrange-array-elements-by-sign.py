class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        new = []
        for i in nums:
            if i <0:
                n.append(i)
                
            else:
                p.append(i)
         
        for i,j in zip(p,n):
            new.append(i)
            new.append(j)
            
        return new
