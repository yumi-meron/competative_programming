class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        minimum = k
        left = 0
        while left+k <len(blocks)+1:
            sub = blocks[left:left+k]
            minimum = min(sub.count('W'),minimum)
            left+=1
        return minimum