class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets = []
        currSub = []
        nums.sort()
        def backtrack(idx):
            if idx >= len(nums):
                if currSub not in subsets:
                    subsets.append(currSub[:])
                return


            currSub.append(nums[idx])
            backtrack(idx + 1)

            currSub.pop()
            backtrack(idx + 1)

        backtrack(0)
        return subsets
        