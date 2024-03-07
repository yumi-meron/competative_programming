class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(k):
            hours = 0
            i = 0
            while i < len(piles) and hours <= h:
                hours += math.ceil(piles[i] / k)
                
                i+=1

            return i == len(piles) and hours <= h
        
        minn = 1
        maxx = max(piles)
        ans = maxx
        while minn <= maxx:
            mid = (minn + maxx)//2
            if check(mid):
                ans = mid
                maxx = mid - 1
            else:
                minn = mid + 1
        return ans
