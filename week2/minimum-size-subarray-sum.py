class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left, length,summ = 0,float('inf'),0
      

        for right in range(len(nums)):
            summ += nums[right]
            
            while summ >= target:
                length = min(length, right - left + 1)
                summ -= nums[left]
                left += 1
            
        return length if length != float('inf') else 0

            
            

        