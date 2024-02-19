class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        mp = {'*', '/', '+', '-'}
        for token in tokens:
            if token in mp:
                x = stack.pop()
                y = stack.pop()
                if token == '*':
                    stack.append(x*y)
                elif token == '/':
                    stack.append(int(y/x))
                elif token == '-':
                    stack.append(y-x)
                elif token == '+':
                    stack.append(y+x)
            else:
                stack.append(int(token))
           
        return stack[-1]
        






        