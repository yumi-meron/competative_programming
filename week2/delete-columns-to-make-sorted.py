class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        lst = list(zip(*strs))
        count = 0
        for i in range(len(lst)):
            temp = ''.join(lst[i])
            if temp != ''.join(sorted(temp)):
                count += 1
        return count
        