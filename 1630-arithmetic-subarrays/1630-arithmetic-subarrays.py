import numpy as np
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i,j in zip(l,r):
            sub = sorted(nums[i:j+1])
            diff = sub[1]- sub[0]
            for k in range(len(sub)-1):
                if sub[k+1]-sub[k] != sub[1]-sub[0]:
                       ans.append(False)
                       break
            else:
                ans.append(True)
        return ans
             
                
            
            
        