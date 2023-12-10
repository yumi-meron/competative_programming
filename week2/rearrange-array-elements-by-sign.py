class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p =0
        n =1 
        new = [0]*len(nums)
        for i in nums:
            if i<0:
                new[n] = i
                n+=2
            else:
                new[p] = i
                p+=2
        return new
