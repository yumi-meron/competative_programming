class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i= 0
        j = 1
        while j < len(nums) and i<len(nums):
            if nums[i] == 0:
                if nums[j]==0:
                    j+=1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    i+=1
                    j+=1
            else:
                i+=1
                j+=1
        return nums
                
                
            
            
        