class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mp = {
            2: ['a', 'b', 'c'],
            3: ['d', 'e', 'f'],
            4: ['g', 'h', 'i'],
            5: ['j', 'k', 'l'], 
            6: ['m', 'n', 'o'], 
            7: ['p', 'q', 'r', 's'],
            8: ['t', 'u', 'v'], 
            9: ['w', 'x', 'y', 'z']
        }
        ans = []
        curr = []

        def backtrack(idx):
            if len(curr) == len(digits):
                ans.append(''.join(curr))
                return 

            if idx > len(digits):
                return
            for char in mp[int(digits[idx])]:
                curr.append(char)
                backtrack(idx+1)
                curr.pop()
        if not digits:
            return []
        backtrack(0)
        return ans

                
        