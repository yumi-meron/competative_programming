class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        left, count , maxx, ones = 0,0,0, 0

        for right in range(len(nums)):

            if nums[right] == 0:
                count += 1
            elif nums[right] == 1:
                ones += 1

            maxx = max(maxx,ones)
            if count > 1:
                while count > 1:
                    if nums[left] == 0:
                        count -= 1
                    else:
                        ones -= 1
                    left += 1
        if count == 0:
            maxx -= 1

            
        return maxx
                    


        