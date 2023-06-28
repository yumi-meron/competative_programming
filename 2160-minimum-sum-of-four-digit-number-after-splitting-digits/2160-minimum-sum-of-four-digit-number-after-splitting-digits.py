class Solution:
    def minimumSum(self, num: int) -> int:
        nums = list(map(int, str(num)))
        nums.sort(reverse = True)
        num1 = int(str(nums[-1]) + str(nums[0]))
        num2 = int(str(nums[2]) + str(nums[1]))
        
        
        return num1+num2
        
        