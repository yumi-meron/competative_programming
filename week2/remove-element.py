class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length =  len(nums)
        val_count = nums.count(val)
        for left in range(length - val_count):

            if nums[left] == val:
                right = left
                while nums[right] == val:
                    right += 1
                    
                nums[left], nums[right] = nums[right], nums[left]

        return length - val_count




        