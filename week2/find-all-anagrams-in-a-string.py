class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        check = sorted(p)
        ans = []
        left = 0

        for right in range(len(p), len(s)+1):
            if sorted(s[left:right]) == check:
                ans.append(left)
            left += 1

        return ans

        