class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        myset = {i for a,b in ranges for i in range(a,b+1)}
    
        return True if set(range(left,right+1)) <= (myset) else False
        