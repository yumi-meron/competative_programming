class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for p in path:
            if stack and p == '..':
                stack.pop()
            elif p != '.' and p != '..' and p != '':
                stack.append(p)
        temp = []
        if not stack: return "/"
        while stack:
            temp.append(stack.pop())
            temp.append('/')
        stack = temp[::-1]

        return ''.join(stack)

        