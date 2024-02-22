class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = [] 
        mp = {}
        for num in nums2:
            while stack and stack[-1] < num:
                key = stack.pop()
                mp[key] = num
            stack.append(num)
        ans = [-1] * len(nums1)
        for i in range(len(nums1)):
            if nums1[i] in mp:
                ans[i] = mp[nums1[i]]
        return ans
