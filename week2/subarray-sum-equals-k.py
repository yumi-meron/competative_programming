class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        ans = 0
        runsum = 0
        for num in nums:
            runsum += num
            diff = runsum - k
            ans += mp.get(diff,0)
            mp[runsum] = mp.get(runsum,0) + 1
        return ans


