class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        x = 0
        for i in range(len(nums)):
            nums.sort()
            if nums[i] != x:
                x = i
                break
            x += 1
        return x   
            
        
            