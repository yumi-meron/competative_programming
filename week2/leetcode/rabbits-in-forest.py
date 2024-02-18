class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = Counter(answers)
        ans = 0
        for x in count:
            ans += (count[x] + x) // (x + 1) * (x + 1)
        return ans
      