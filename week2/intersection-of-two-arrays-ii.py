class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i, j = 0, 0
        ans = []
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                ans. append(nums1[i])
                i+=1
                j+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                i+=1
        return ans


        # counter1 = Counter(nums1)
        # counter2 = Counter(nums2)
        # ans = []
        # for key in counter1:
        #     if key in counter2:
        #         minn = min(counter1[key], counter2[key])
        #         ans += [key] * minn
        # return ans
