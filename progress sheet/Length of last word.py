class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        sentence = s.rstrip()
        word = sentence.split(" ")
        length = len(word[-1])
        return length
