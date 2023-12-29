class Solution:
    def sortSentence(self, s: str) -> str:
        count =[0] *10
        s = list(s.split(" "))
        for word in s:
            count[int(word[-1])-1] = word[:-1]
        j = 0
        for i in range(len(count)):
            if count[i]:
                s[j] = count[i]
                j+=1
        return ' '.join(s)
        