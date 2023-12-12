class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        counter = Counter(arr)
        n = len(arr) // 4
        for count in counter:
            if counter[count] > n:
                return count
        
        