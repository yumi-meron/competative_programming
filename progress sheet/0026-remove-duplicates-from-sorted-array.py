class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        y = 1
        z=nums[-1]
        while nums[x] != z:
            if nums[x] == nums[y]:
                nums.append(nums[y])
                nums.pop(y)
                
            else:
                x+=1
                y+=1
        return(len(nums[:nums.index(z)+1]))
            
            
        