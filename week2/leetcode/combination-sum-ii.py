class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        summ = 0
        ans =  []
        combs = []
        prev = None
        def backtrack(idx, summ):
            nonlocal prev
            if summ == target: #and combs not in ans:
                ans.append(combs[:])
                return
            if summ > target:
                return 

            while idx < len(candidates) and candidates[idx] == prev:
                idx += 1
                
            if idx >= len(candidates):
                return
            summ += candidates[idx]
            combs.append(candidates[idx])
            backtrack(idx +1, summ)

            summ -= candidates[idx]
            prev = combs.pop()
            backtrack(idx + 1, summ)
        
        backtrack(0,0)
        return ans

