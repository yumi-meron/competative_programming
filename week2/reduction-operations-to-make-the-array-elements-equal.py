class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        inc = 0
        ans = 0
        for i in range(1,len(nums)):
            if nums[i-1] < nums[i]:
                inc += 1
            ans += inc
        
        return ans

        