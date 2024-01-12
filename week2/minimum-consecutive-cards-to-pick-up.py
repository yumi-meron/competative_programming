class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        left, ans = 0, float('inf')
        sett = set()
        for right in range(len(cards)):
            while cards[right] in sett:
                ans = min(ans, right - left + 1)
                sett.remove(cards[left])
                left += 1

            sett.add(cards[right])
            

        if len(sett) == len(cards): return -1
        return ans
        