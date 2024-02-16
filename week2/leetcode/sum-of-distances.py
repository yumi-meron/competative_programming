class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        ans = [0] * len(nums)

        preSum = defaultdict(int)
        preCount = defaultdict(int)

        for i, val in enumerate(nums):
            ans[i] += i * preCount[val]
            ans[i] -= preSum[val]

            preSum[val] += i
            preCount[val] += 1
        
        postSum = defaultdict(int)
        postCount = defaultdict(int)

        for i, val in reversed(list(enumerate(nums))):
            ans[i] += postSum[val]
            ans[i] -= i * postCount[val]
            
            postSum[val] += i
            postCount[val] += 1
            
        return ans
        