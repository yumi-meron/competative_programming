class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort(reverse = True)
        count = [0]*(len(nums)+1)
        for rq in requests:
            start, end = rq
            count[start] += 1
            count[end + 1] -= 1
        for i in range(1,len(count)):
            count[i] += count[i-1] 

        count.sort(reverse = True)

        ans = 0
        for i in range(len(nums)):
            ans += (count[i] * nums[i])
        
        return ans % ((10 ** 9) + 7)


        