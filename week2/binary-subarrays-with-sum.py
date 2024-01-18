class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        mp = {0:1}
        runsum = 0
        ans = 0
        for num in nums:
            runsum += num
            x = runsum - goal
            ans += mp.get(x,0)
            mp[runsum] = mp.get(runsum, 0 ) + 1
        return ans
            