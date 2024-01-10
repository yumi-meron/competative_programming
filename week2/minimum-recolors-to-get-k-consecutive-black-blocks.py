class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        curr = Counter(list(blocks[:k-1]))
        left, ans =0,  float('inf')
        for right in range(k-1,len(blocks)):
            curr[blocks[right]] = curr.get(blocks[right], 0) + 1
            w = curr.get('W', 0)
            ans = min(ans, w)
            if curr[blocks[left]] -1 ==0:
                del curr[blocks[left]]
            else:
                curr[blocks[left]] -= 1
            left += 1
        return ans

        