class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(capacity):
            idx = 0            
            for i in range(days):
                weight = 0
                while idx < len(weights) and weight + weights[idx] <= capacity:
                    weight += weights[idx]
                    idx += 1
            if idx < len(weights):
                return False
            return True
         
        minn,maxx = min(weights), sum(weights)
        ans = maxx
        while minn <= maxx:
            mid = (minn + maxx) // 2
            result = check(mid)
            if result:
                ans = mid
                maxx = mid - 1
            elif not result:
                minn = mid + 1
            # if minn == maxx:
            #     return minn
        return ans


            

                
