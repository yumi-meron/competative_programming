class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1]*len(nums)
        prefix = 1
        for i in range(len(nums)):
            answer[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for j in range(len(nums)-1,-1,-1):
            answer[j] *= postfix
            postfix *= nums[j]
        return answer
            
            
            
        
        