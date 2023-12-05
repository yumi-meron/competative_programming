class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        ans = [True if candy + extraCandies >= greatest else False for candy in candies]
        return ans
        