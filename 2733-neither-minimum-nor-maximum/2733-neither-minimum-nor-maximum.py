class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        nums.sort()
        if nums[len(nums)//2] != nums[0] and nums[len(nums)//2] != nums[-1]:
            return nums[len(nums)//2]
       
            
        