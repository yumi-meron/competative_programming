class Solution:
    def shortestSequence(self, rolls: List[int], k: int) -> int:
        mp = {}
        val = 0
        for roll in rolls:
            mp[roll] = mp.get(roll, 0) + 1
            if len(mp) == k:
                val += 1
                mp.clear()
        return val + 1