class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        #check is variable for checking if  we have more than one out of order number
        check = 0
        
        for i in range(1,len(nums)):
            if nums[i] < nums[i-1]:
                if check > 0:
                    return False
                elif i < 2 or nums[i-2] <= nums[i]:
                    nums[i-1] = nums[i]
                else:
                    nums[i] = nums[i-1]
                check += 1
        return True

        