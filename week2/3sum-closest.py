class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        minn = float('inf')
        ans = 0
        for i in range(len(nums)):
            j,k = i+1, len(nums)-1
            while j<k:
                summ = nums[i] + nums[j] + nums[k]
                if abs(summ - target) < minn:
                    minn = abs(summ - target)
                    ans = nums[i] + nums[j] + nums[k]
                   
                if summ < target:
                    j+=1
                else:
                    k-=1
        return ans
        