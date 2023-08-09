class Solution:
    def removeStars(self, s: str) -> str:
        arr = []
        i = 1
        for i in s:
            if i != '*':
                arr.append(i)
            else:
                if arr is not None:
                    arr.pop()
        return "".join(arr)
        