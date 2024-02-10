class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        left, maxx, summ = 0,float('-inf'),0
        for right in range(len(nums)):
            summ += nums[right]
            maxx = max(maxx, summ)
            while summ < 0:
                summ -= nums[left]
                left += 1
            # maxx = max(maxx, summ)
        return maxx

        