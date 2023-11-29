class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = float('inf')
        left = 0
        the_sum = 0
        for right in range(len(nums)):
            the_sum += nums[right]
            while the_sum >= target:
                ans = min(ans, right-left+1)
                the_sum -= nums[left]
                left+=1
                
        return ans if ans != float(inf) else 0
                
            
        