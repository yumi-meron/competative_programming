class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = [1] * len(nums)
        preproduct = 1
        for i in range(len(nums)):
            answer[i] *= preproduct
            preproduct *= nums[i]
            
        postproduct = 1
        for j in range(len(nums)-1,-1,-1):
            answer[j] *= postproduct
            postproduct *= nums[j]

        return answer
        