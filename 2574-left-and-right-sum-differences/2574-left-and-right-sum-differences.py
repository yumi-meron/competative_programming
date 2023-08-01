class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = []
        right = []
        ans = []
        for i in range(len(nums)):
            if i == 0:
                
                ans.append(abs(sum(nums[i+1:])))
            elif i == len(nums)-1:
                
                ans.append(abs(sum(nums[:i])))
            else:
               
                ans.append(abs(sum(nums[:i])-sum(nums[i+1:])))
        return ans
            
        
        