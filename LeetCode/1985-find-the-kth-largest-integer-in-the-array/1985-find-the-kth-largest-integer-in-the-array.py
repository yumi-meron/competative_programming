class Solution(object):
    def kthLargestNumber(self, nums, k):
        """
        :type nums: List[str]
        :type k: int
        :rtype: str
        """
        int_list = [eval(i) for i in nums]
        largest_int = str(sorted(int_list)[-k])
        return largest_int
