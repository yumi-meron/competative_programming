class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        presum = 0
        for i in nums:
            ans.append(presum+i)
            presum += i
        return ans