class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        dic = {}
        for i, val in enumerate(order):
            dic[val] = i
        
        for i in range(len(words)-1):
            for j in range(len(words[i])):
                if j>=len(words[i+1]):
                    return False 
                elif dic[words[i][j]] < dic[words[i+1][j]]:
                    break
                elif dic[words[i][j]] > dic[words[i+1][j]]:
                    return False
        return True
        