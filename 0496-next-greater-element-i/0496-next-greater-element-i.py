class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        for num in nums1:
            x = nums2.index(num)
            for i in range(x,len(nums2)):
                if nums2[i] > num:
                    stack.append(nums2[i])
                    break
            else:
                stack.append(-1)
        return stack
        