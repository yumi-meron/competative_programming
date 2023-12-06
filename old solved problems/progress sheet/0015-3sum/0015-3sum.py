class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        for i, a in enumerate(nums):
            if i > 0 and a == nums[i-1]:
                continue
           
            l, r = i+1, len(nums)-1
            while l<r:
                sm = a + nums[l] + nums[r]
                if sm>0:
                    r-=1
                elif sm<0:
                    l+=1
                else:
                    ans.append([a,nums[l],nums[r]])
                    l+=1
                    while  l<r and nums[l] == nums[l-1]:
                        l+=1
                
        return ans      
                    
        
                
                
            
        