class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        k = 0
        for i,j in zip(heights,expected):
            if i!=j:
                k+=1
        return k

        