class Solution(object):
    def maxOperations(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        counter = defaultdict(int)
        op_ = 0
        for x in nums:
            y  = k-x
            if counter[y]>0:
                counter[y]-=1
                op_ +=1
            else:
                counter[x]+=1
        return op_
        