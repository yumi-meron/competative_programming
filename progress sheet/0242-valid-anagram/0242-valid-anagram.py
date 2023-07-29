class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        string_s = sorted([str(x) for x in s])
        string_t = sorted([str(x) for x in t])
        if len(s) != len(t):
            return False
        return string_s == string_t
                
            
        