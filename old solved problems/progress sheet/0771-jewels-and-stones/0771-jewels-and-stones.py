class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        st = list(jewels)
        count = 0
        for i in range(len(stones)):
            if stones[i] in st:
                count +=1
        return count
        