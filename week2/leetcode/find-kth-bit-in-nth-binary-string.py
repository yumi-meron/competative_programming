class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def func(n):
            if n == 0:
                return ['0']
            prev = func(n-1)
            curr = prev.copy()
            curr.append('1')
            new = ['0' if i == '1' else '1' for i in prev ]
            new = new[::-1]
            curr.extend(new)
            return curr
        # print(func(n-1))
        return func(n-1)[k-1]
    