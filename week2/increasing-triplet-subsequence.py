class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        n = len(nums)
        left = float('inf')
        mid = float('inf')
        for i in range(n):
            if nums[i] < mid and  nums[i]>left:
                mid = nums[i]
            elif nums[i] < left  :
                left = nums[i]
            elif nums[i] > left and nums[i] > mid:
                return True
        return False

            

        


            
        