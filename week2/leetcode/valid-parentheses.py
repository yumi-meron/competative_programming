class Solution:
    def isValid(self, s: str) -> bool:
        mp = {')':'(', ']':'[', '}':'{'}
        stack = []
        for b in s:
            if b in mp:
                if not stack or mp[b] != stack.pop():
                    return False
            else:
                stack.append(b)
        return len(stack) == 0
        