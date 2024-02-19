class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(list(s))
        letters = 0
        odd = 0
        for key in counter:
            if counter[key] % 2 == 0:
                letters += counter[key]
            else:
                letters += (counter[key] - 1)
                odd = 1
        if odd: letters += 1
        return letters
        