class Solution(object):
    def dividePlayers(self, skill):
        """
        :type skill: List[int]
        :rtype: int
        """
        skill.sort()
        i = 0
        j = len(skill)-1
        players = set()
        chem = 0
        while i<j:
            players.add((skill[i]+skill[j]))
            chem += (skill[i]*skill[j])
            i+=1
            j-=1
        if len(players) == 1:
            return chem
        else:
            return -1
            
        
        