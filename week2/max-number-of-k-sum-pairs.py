class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums.sort()
        i,j = 0, len(nums)-1
        op = 0
        while i<j:
            if nums[i] + nums[j] == k:
                op,i,j = op+1, i+1,j-1
            elif nums[i] + nums[j] < k:
                i+=1
            else:
                j-=1
        return op
            
        