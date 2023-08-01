class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most = 0
        for sentence in sentences:
            words = sentence.split()
            count = len(words)
            most = max(count, most)
        return most