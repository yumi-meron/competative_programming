class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        leftsum ,rightsum = 0,sum(nums)

        for i in range(len(nums)):
            rightsum -= nums[i]
            diff = ((nums[i] * i) - leftsum) + (rightsum - (nums[i] * (n-i-1)))
            ans.append(diff)
            leftsum += nums[i]
            
        return ans
        