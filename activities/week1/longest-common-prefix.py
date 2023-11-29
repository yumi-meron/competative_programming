class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = []
        strs.sort()
        flag = 0
        if len(strs) <2:
            return strs[0]
        for i in range(len(strs[0])):
            for j in strs[1:]:

                if j[i] != strs[0][i]:
                    flag = 1
                    break
            else:
                ans.append(j[i])
            if flag == 1:
                break
        return ''.join(ans)
        