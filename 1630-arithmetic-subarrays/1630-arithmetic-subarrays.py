import numpy as np
class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        ans = []
        for i,j in zip(l,r):
            sub = sorted(nums[i:j+1])
            diff = sub[1]- sub[0]
            if all(sub[k+1]-sub[k] == diff for k in range(len(sub)-1)):
                ans.append(True)
            else:
                ans.append(False)
        return ans
             
                
            
            
        