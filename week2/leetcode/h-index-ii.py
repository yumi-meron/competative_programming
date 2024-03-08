class Solution:
    def hIndex(self, citations: List[int]) -> int:
        # if len(citations) == 1:
        #     return 0 if citations[0] == 0

        ans = 0

        left, right = 0, len(citations) 

        while left <= right:

            mid = (left + right) // 2
            idx = bisect_left(citations, mid)
            elements = len(citations) - idx

            if mid > elements:
                right = mid - 1
            elif mid <= elements:
                ans = mid
                left = mid + 1
            
        return ans


        