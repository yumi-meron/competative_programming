class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        # nums left score = 0's sum
        # nums right score = 1's sum
        #prefix = 4
        # [0,1,0,0,0,1,1,0,1]
        #0:left = 0 right = 4 sum = 4
        #1:left = 1 right = 4 sum = 5
        #2: left = 1 right = 3 sum = 4
        #3: left = 2 right = 3 sum = 5 
        #4: left = 3 right = 3 sum = 6
        #5: left = 4 right = 2 sum = 6
        #6: left = 4 right = 1 sum = 5 
        #7: left = 4 right = 1 sum = 5 
        #8: left = 5 right = 0 sum = 5 
        n = len(nums)
        prefix = sum(nums) 
        zeros = 0 
        ans = []
        maxx = 0
        for i in range(len(nums)+1):
            summ = prefix + zeros
            if i == 0:
                maxx = summ
                ans.append(i)
                if nums[i] == 0:
                    zeros += 1
                else:
                    prefix -= 1
                
            elif i == n:
                if maxx == summ:
                    ans.append(i)
                elif maxx < summ:
                    ans = [i] 
            else:
                if maxx == summ:
                    ans.append(i)
                elif summ > maxx:
                    ans = [i]
                    maxx = summ

                if nums[i] == 0:
                    zeros += 1
                elif nums[i] == 1:
                    prefix -= 1
        return ans
                


