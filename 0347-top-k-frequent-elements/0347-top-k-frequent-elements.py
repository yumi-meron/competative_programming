from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        c = Counter(nums)
        c = sorted(c,key=lambda x:c[x], reverse = True)
    
        return c[:k]  
            