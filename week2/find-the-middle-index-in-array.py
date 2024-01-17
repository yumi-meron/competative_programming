class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        pre = sum(nums)
        runsum = 0
        for i in range(len(nums)):
            pre -= nums[i]
            if runsum == pre:
                return i
            runsum += nums[i]
        return -1
        