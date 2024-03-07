class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect_left(arr, x)
        # print(idx)
        if idx == 0:
            return arr[:k]
        if idx == len(arr):
            return arr[len(arr)-k:]
        l = idx - 1
        r = idx 
        ans = []
        while l >=0 or r < len(arr):
            if len(ans) == k:
                break
            curr = None
            if l < 0:
                curr = arr[r]
                r+=1
            elif r >= len(arr):
                curr = arr[l]
                l-=1
            else:
                if abs(arr[l] - x) <= abs(arr[r] - x):
                    curr = arr[l]
                    l-=1
                else:
                    curr = arr[r]
                    r += 1
            ans.append(curr)
        return sorted(ans)
        
                



        
        