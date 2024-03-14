class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        prefix = []
        for i,val in enumerate(s):
            if val == '|':
                prefix.append(i)
        ans = []
        for left, right in queries:
            left_most = bisect_left(prefix, left)
            right_most = bisect_right(prefix, right) - 1
            curr = (prefix[right_most] - prefix[left_most]) - (right_most - left_most) if left_most < right_most else 0
            ans.append(curr)
        return ans



        
        