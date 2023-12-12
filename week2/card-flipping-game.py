class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        invalid = set()
        for n1,n2 in zip(fronts,backs):
            if n1 == n2:
                invalid.add(n1)
        ans = []
        for i in range(len(fronts)):
            if fronts[i] not in invalid:
                ans.append(fronts[i])
            if backs[i] not in invalid:
                ans.append(backs[i])
        return min(ans) if ans else 0
            
        
