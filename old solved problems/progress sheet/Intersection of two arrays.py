from collections import Counter 
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        intersection = counter1 & counter2 
        keys = list(intersection.keys())
        return keys
