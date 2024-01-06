class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if len(nums) == 1:
            return nums[0]/1

        summ = sum(nums[:k])
        avg = summ/k
        left = 0
        right = k

        while right < len(nums):
            summ += nums[right]
            summ -= nums[left]
            avg = max(avg, summ/k)
            left += 1
            right += 1

        return avg

        