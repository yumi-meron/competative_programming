class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        dic = {val:i for i,val in enumerate(nums)}
        for num,val in operations:
            index = dic.get(num)
            if index is not None:
                nums[index] = val
                dic[val] = index
                del dic[num]
            
        return nums
        
        