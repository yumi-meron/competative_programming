class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(list(s))
        stack = []
    
        for char in s:
            if stack and ord(stack[-1])  > ord(char):
                while stack and char not in stack and ord(stack[-1])  > ord(char) and (counter[stack[-1]] - 1) > 0:
                    counter[stack.pop()] -= 1
                if char not in stack:
                    stack.append(char) 
                else:
                    counter[char] -= 1
                # else:
                #     continue
            else:
                if char not in stack:
                    stack.append(char)
                else:
                    counter[char] -= 1
        return ''.join(stack)


        