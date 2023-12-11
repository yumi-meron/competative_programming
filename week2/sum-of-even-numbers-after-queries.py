class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        summ = 0
        for num in nums:
            if num % 2 == 0:
                summ += num
        ans = []
        for val, ind in queries:
            prev = nums[ind]
            nums[ind] += val
            curr = nums[ind]
            if prev % 2 == 0:
                if curr % 2 == 0:
                    summ += (curr - prev)
                else:
                    summ -= prev
            else:
                if curr % 2 == 0:
                    summ += curr
            ans.append(summ)

        return ans
        