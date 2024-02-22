class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        ans = [-1] * len(nums)
        for i, num in enumerate(nums):
            while stack and stack[-1][1] < num:
                val = stack.pop()
                ans[val[0]] = num
            stack.append((i,num))

        
        for num in stack:
            for i in range(len(nums)):
                if nums[i] > num[1]:
                    ans[num[0]] = nums[i]
                    break
            
        return ans




        