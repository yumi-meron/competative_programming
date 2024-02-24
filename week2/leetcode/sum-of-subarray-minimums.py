class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        stack = [] #(ind,val)
        ans = 0
        for i,val in enumerate(arr):
            while stack and stack[-1][1] > val:
                idx, num = stack.pop()
                left = idx - stack[-1][0] if stack else idx + 1
                right = i - idx
                ans += (num * left * right)
            
            stack.append((i, val))
        
        for i in range(len(stack)):
            idx, val = stack[i]
            left = idx - stack[i-1][0] if i > 0 else idx + 1
            right = len(arr) - idx
            ans += (val * left * right)
        return ans % (10 ** 9 + 7)

