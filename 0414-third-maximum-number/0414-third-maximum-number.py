class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        my_set = sorted(set(nums))
        
        if len(my_set)<3:
            return my_set[-1]
        else:
            return my_set[-3]
        