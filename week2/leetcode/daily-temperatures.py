class Solution:
    def dailyTemperatures(self, temper: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temper)

        for i,temp in reversed(list(enumerate(temper))):

            while stack and temper[stack[-1]] <= temp:
                stack.pop()

            if stack:
                ans[i] = stack[-1] - i
                
            stack.append(i)
            
        return ans