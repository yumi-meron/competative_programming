class Solution(object):
    def sortSentence(self, s):
        """
        :type s: str
        :rtype: str
        """
        x = s.split()
        dic = {}
        for i in x:
            dic[i[-1]] = i[:-1]

        return ' '.join(dic[j] for j in sorted(dic))        
