class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        l = len(nums2)
        dic = defaultdict(int)
        for i,n in enumerate(nums2):
            dic[n] =i
        for i in nums1:
            count = 0
            for j in range(dic[i]+1, l):
                if i<nums2[j]:
                    count+=1
                    ans.append(nums2[j])
                    break
            if count == 0:
                ans.append(-1)
        return ans
            