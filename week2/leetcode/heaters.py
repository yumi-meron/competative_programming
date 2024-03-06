class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        def check(capacity):
            l = 0
            r = 0
            while r < len(houses) and l < len(heaters):
                ranges = [heaters[l] - capacity, heaters[l] + capacity]
                # if house[r] >= range[0] and house[r] <= range[1]:
                if houses[r] < ranges[0]:
                    return False
                if houses[r] > ranges[1]:
                    l += 1
                    continue
                r+=1
            return r == len(houses)
        ans = None
        minn = 0
        maxx = max(max(houses), max(heaters))
        while minn <= maxx:
            mid = (minn + maxx) // 2
            if check(mid):
                ans = mid
                maxx = mid - 1
                # check(mid)
            else:
                minn = mid + 1
                # check(mid)
        return ans
