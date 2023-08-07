class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = s[:spaces[0]]
        for i in range(len(spaces)):
            if i <len(spaces)-1:
                ans += " " + s[spaces[i]:spaces[i+1]]
            else:
                ans += " " + s[spaces[i]:]
        return ans
      