class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # return combinations(range(1,n+1),k)
        # nums = [i for i in range(1,n+1)]
        combs = []
        # def backtrack(i, comb):
        #     if len(comb) == k:
        #         combs.append(comb.copy())
        #         return 
        #     if i>=n:
        #         return 
        #     comb.append(nums[i])
        #     backtrack(i+1, comb)

        #     comb.pop()
        #     backtrack(i+1, comb)
        # backtrack(0, [])
        # return combs
        def backtrack(idx, comb):
            if len(comb) == k:
                combs.append(comb.copy())
                return 
            for i in range(idx, n+1):
                comb.append(i)
                backtrack(i+1, comb)
                comb.pop()
        backtrack(1,[])
        return combs            
        