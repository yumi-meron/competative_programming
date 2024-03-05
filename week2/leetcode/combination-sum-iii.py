class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # curr = 1
        currSub = []
        ans = []
        summ = 0
        def backtrack(curr,summ):
            if summ == n and len(currSub) == k:
                ans.append(currSub[:])
                return
                
            if curr > 9 or len(currSub) >= k or summ > n:
                return
            
            summ += curr
            currSub.append(curr)
            backtrack(curr+1,summ)

            summ -= curr
            currSub.pop()
            backtrack(curr+1,summ)
        backtrack(1, 0)
        return ans
            

        