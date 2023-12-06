class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split()
        reversed_word = [''.join(reversed(word))for word in words]
        reversed_s = ' '.join(reversed_word)
        return reversed_s