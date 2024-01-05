class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0]*3
        for num in nums:
            counter[num] += 1
        pos = 0
        for i in range(len(counter)):
            while counter[i] > 0:
                nums[pos] = i
                pos += 1
                counter[i] -= 1
        return nums
            
            
        