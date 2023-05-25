class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        smallers = list()
        for i in range(len(nums)):
            small = 0
            for j in range(len(nums)):
                if nums[j] < nums[i]:
                    small += 1
            smallers.append(int(small))
        return smallers
        
