class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        ans = []
        i = 0
        j = len(nums)-1
        lst = sorted(nums)
        while i<j:
            ans.append(lst[i]+lst[j])
            i+=1
            j-=1
        return max(ans)