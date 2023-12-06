class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        num_of_ones = []
        temp = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                temp+=1
            else:
                num_of_ones.append(temp)
                temp = 0
        if temp:
            num_of_ones.append(temp)
        return max(num_of_ones)
            


        