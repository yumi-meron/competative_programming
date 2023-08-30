class Solution:
    def decodeString(self, s: str) -> str:
        if not s:
            return ""
        stack = []
        for c in s:
            if c == ']':
                encoded = ""
                while stack and stack[-1]!='[':
                    encoded = stack.pop() + encoded
                    
                stack.pop()
                k = ''
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                k = int(k)
                
                stack.append(encoded * k)
                
            else:
                stack.append(c)
        return "".join(stack)
                    
                
            