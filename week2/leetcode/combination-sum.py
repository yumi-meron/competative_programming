class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        combs = []
        def backtrack(i, summ):
            if summ == target:
                ans.append(combs[:])
                return
            if summ > target:
                return 
            if i >= len(candidates):
                return
            # for i in range(len(candidates)):
            # print(summ)
            summ += candidates[i]
            combs.append(candidates[i])

            backtrack(i, summ)

            summ -= candidates[i]
            combs.pop()
            backtrack(i+1, summ)
            return
              

        backtrack(0, 0)
        return ans

