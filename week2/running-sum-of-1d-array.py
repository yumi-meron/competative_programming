class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        runsum = 0
        for num in nums:
            runsum += num
            ans.append(runsum)
        return ans
            
