class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        mp = defaultdict(list)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                mp[i+j].append(mat[i][j])
        ans = []
        for key in mp:
            if key%2:
                ans += mp[key]
            else:
                ans += reversed(mp[key])
        return ans

        
        