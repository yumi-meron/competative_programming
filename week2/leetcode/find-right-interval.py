class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        sorted_arr = sorted(intervals)
        starts = [val[0] for val in intervals]
        mp = {val: i for i,val in enumerate(starts)}
        starts.sort()
        
        
        ans = []
        for interval in intervals:
            start, end = interval
            idx = bisect_left(starts, end)
            if idx >= len(starts):
                ans.append(-1)
            else:
                ans.append(mp[starts[idx]])
            

        return ans
        