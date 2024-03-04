class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        def backtrack(i, currsub):
            if i >= len(nums):
                subsets.append(currsub.copy())
                return

            currsub.append(nums[i])

            backtrack(i+1,currsub)

            currsub.pop()

            backtrack(i+1, currsub)
            
        backtrack(0, [])
        return subsets
        
    
            
        