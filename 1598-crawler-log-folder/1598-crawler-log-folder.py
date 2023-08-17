class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0
        for i in logs:
            if i == "./":
                continue
            elif i == "../":
                depth -= 1
                if depth<0:
                    depth = 0
            else:
                depth+=1
        return depth