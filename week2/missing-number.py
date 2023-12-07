class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        myset = set(nums)
        return [num for num in range(len(nums)+1) if num not in myset][0]
        """
        for num in range(len(nums)+1):
            if num not in myset:
                return num

        """

        

        