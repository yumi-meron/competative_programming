class Solution:
    def dailyTemperatures(self, temper: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temper)

        # for i,temp in reversed(list(enumerate(temper))):

        #     while stack and temper[stack[-1]] <= temp:
        #         stack.pop()

        #     if stack:
        #         ans[i] = stack[-1] - i
                
        #     stack.append(i)
        for i,temp in enumerate(temper):
            while stack and temper[stack[-1]] < temp:
                prev = stack.pop()
                ans[prev] = i - prev

            stack.append(i)
            
        return ans