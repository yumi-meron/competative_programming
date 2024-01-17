class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # pre = [nums[0]] * len(nums)
        ans = 0
        mp = {0:1}
        runsum = 0
        print(-9%5)
        for i in range(len(nums)):
            runsum += nums[i]
            remainder = runsum % k
            ans += mp.get(remainder, 0)
            
            mp[remainder] = mp.get(remainder, 0) + 1
        return ans

             


            
            
        