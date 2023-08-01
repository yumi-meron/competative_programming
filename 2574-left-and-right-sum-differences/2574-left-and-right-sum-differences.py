class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left = 0
        right = sum(nums)
        ans = []
        for i, num in enumerate(nums):
            right -= num
            ans.append(abs(right-left))
            left +=num
        return ans
            
            