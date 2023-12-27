class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = [0] * (max(nums)+1)
        for i in range(len(nums)):
            temp[nums[i]] += 1
        mp = {}
        pre = 0
        for i in range(len(temp)):
            if temp[i] != 0:
                mp[i] = pre
                pre += temp[i]
        ans = []
        for num in nums:
            ans.append(mp[num])
        return ans 
        