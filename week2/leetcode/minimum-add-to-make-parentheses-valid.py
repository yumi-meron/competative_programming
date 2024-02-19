class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        ans = 0
        for letter in s:
            if letter == ')':
                if stack:
                    stack.pop()
                else:
                    ans += 1
            else:
                stack.append(letter)
        ans += len(stack)

        return ans
        