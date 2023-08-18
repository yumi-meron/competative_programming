class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        ans = [""]
        s = path.split('/')
        for i in s:
            if stack and i == '..':
                stack.pop()
            elif i != '' and i != '.' and i!='..':
                stack.append(i)
        if not stack:
            return('/')
        while stack:
            ans.insert(0, stack.pop())
            ans.insert(0,'/')
        return ''.join(ans)
            