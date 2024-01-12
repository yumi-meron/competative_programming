class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        left, count, countOdd,ans = 0, 0, 0, 0
        
        for right in range(len(nums)):
            if nums[right] % 2:
                countOdd += 1
                count = 0
            
            while countOdd == k:
                countOdd -= int(nums[left]%2)
                count += 1
                left += 1
            
            ans += count
            


  
        return ans

