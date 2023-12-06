class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        temp = ""
        for i in s :
            if i != ')':
                stack.append(i)
            else:
                while stack[-1] != '(':
                    temp += stack.pop()
                stack.pop()
                for char in temp:
                    stack.append(char)
                temp = ""
        return ''.join(stack)
            
