class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        #[1,12,-5,-6,50,3]
        #[1,12,-5,-6]
        #[12,-5,-6,50]
        #[-5,-6,50,3]
        max_val = now = sum(nums[:k])
        for i in range(k,len(nums)):
            now +=  nums[i] - nums[i-k]
            if now>max_val: max_val = now
            
        return max_val / k
            
            
            
        
        