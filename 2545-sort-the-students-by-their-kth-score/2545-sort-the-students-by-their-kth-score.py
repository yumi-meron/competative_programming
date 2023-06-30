import numpy as np
class Solution(object):
    def sortTheStudents(self, score, k):
        """
        :type score: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        
        a = np.array(score)
        a= a[a[:,k].argsort()[::-1]]
        return a