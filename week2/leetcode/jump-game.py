class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        steps = 0
        if n==1: return True
        for i in range(n):
            steps = max(steps, i+nums[i])
            if i == steps:
                return False
            if steps >= n-1:
                return True
        
        

        