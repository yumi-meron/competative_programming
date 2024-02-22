class Solution:
    def minOperations(self, logs: List[str]) -> int:
        stack = []
        for log in logs:
            if stack and log == "../":
                stack.pop()
            elif log != "./" and log != "../":
                stack.append(log)
        count = 0
        while stack:
            count += 1
            stack.pop()
        return count
        