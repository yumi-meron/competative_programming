class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        currSub = []

        def backtrack():
            if len(currSub) == len(nums):
                ans.append(currSub[:])
                return
            for num in nums:
                if num not in currSub:
                    currSub.append(num)
                    backtrack()
                    currSub.pop()
            # print(currSub)
        backtrack()
        return ans

            
        