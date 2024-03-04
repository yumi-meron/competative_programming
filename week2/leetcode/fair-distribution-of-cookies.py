class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childrens = [0] * k
        min_unfair = float('inf')
        def backtrack(idx):
            nonlocal min_unfair
            if idx >= len(cookies):
                min_unfair = min(min_unfair,max(childrens))
                return
            if max(childrens) > min_unfair:
                return

            for j in range(k):
                childrens[j] += cookies[idx]
                backtrack(idx+1)
                childrens[j] -= cookies[idx]
        
        backtrack(0)
        return min_unfair

        