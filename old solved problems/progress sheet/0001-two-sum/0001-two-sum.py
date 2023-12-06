class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, element in enumerate(nums):
            x = target - element
            if x in dic:
                return [dic[x],i]
            dic[element] = i
        return []
        