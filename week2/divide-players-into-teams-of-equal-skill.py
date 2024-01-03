class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        skill.sort()
        n = len(skill)
        ans = 0
        i,j = 0, n-1
        summ = skill[i] + skill[j]
        while i<j:
            if skill[i] + skill[j] != summ:
                return -1
            else:
                ans += (skill[i] * skill[j])
                i+=1
                j-=1
        return ans


        