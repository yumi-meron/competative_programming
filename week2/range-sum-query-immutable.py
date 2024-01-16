class NumArray:

    def __init__(self, nums: List[int]):
        self.lst = nums
        self.prefix = [0]
        self.runsum = 0
        for i in range(len(nums)):
            self.runsum += nums[i]
            self.prefix.append(self.runsum)

        

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
        

        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)