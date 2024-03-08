class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def check(divisor):
            summ = 0
            for num in nums:
                summ += math.ceil(num/divisor)
            if summ <= threshold:
                return True
            return False
        
        left = 1
        right = max(nums)
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans

        