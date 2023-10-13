class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        x = len(nums)-1
        while i < x and j>i:
            if nums[i] == nums[j]:
                nums.remove(nums[j])
                x -=1    
            else:
                i+=1
                j+=1
        return len(nums)
        