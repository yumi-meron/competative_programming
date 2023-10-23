class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left = 0
        count = 0
        longestWindow = 0
        for i in range(len(nums)):
            if nums[i]==0:
                count+=1
                while count>1:
                    count -= (nums[left]==0)
                    left +=1
            longestWindow = max(longestWindow, i-left)
        return longestWindow
                
                    
            
            
        