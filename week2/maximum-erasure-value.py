class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        left, summ,maxx, sett = 0,0,0,set()
        for right in range(len(nums)):
            while nums[right] in sett:
                summ -= nums[left]
                sett.remove(nums[left])
                left += 1
            sett.add(nums[right])
            summ += nums[right]
            maxx = max(maxx, summ)
        return maxx


        