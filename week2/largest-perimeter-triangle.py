class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        #if the number of sides less than 3 return 0, because a triange have 3 sides
        if len(nums)<3:
            return 0
        #revrse sort our list to have the largest numbers before the smallers
        nums.sort(reverse=True)
        #check for a number that is greater than two other numbers but less than their sum
        for i in range(len(nums)-2):
            if nums[i] < nums[i+1] + nums[i+2]:
                return nums[i] + nums[i+1] + nums[i+2]
                
        #return 0 if there are no such numbers 
        return 0
        