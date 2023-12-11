class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for i, element in enumerate(nums):
            x = target - element
            if x in dic:
                return [dic[x],i]
            dic[element] = i
        return []
        
        