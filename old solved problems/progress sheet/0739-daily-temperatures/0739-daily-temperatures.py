class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        stack = []
        ans = [0]*n
        
        for i,t in enumerate(temp):
            while stack and temp[stack[-1]]<t:
                pre_index = stack.pop()
                ans[pre_index] = i - pre_index
            stack.append(i)
        return ans
        
            
        