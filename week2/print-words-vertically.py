class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word)for word in words) #finding the the longest word length
        
        # paddind each word with space at the end so that all words have the same length as the longest oen
        for i in range(len(words)):
            words[i] += " " * (max_len - len(words[i]))

        # concatination all the letter at spacific index and adding it to our answer after removing trailing spaces
        ans = []
        for i in range(max_len):
            ans.append(''.join(word[i] for word in words).rstrip())
        
        return ans


        
            

        
        