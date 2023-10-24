class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        N = len(arr)
        ans = 1
        anchor = 0
        for i in range(1, N):
            if arr[i-1] < arr[i]:
                c = -1
            elif arr[i-1] > arr[i]:
                c = 1
            else:
                c = 0

            if c == 0:
                anchor = i
            elif i == N-1 or c * ((arr[i] > arr[i+1]) - (arr[i] < arr[i+1])) != -1:
                ans = max(ans, i - anchor + 1)
                anchor = i
        return ans
            
        
        