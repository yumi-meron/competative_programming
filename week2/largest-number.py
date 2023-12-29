class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        lst = [str(num) for num in nums]
        lst.sort(key = lambda x : x * 10)

        return ("".join(lst[::-1])).lstrip('0') or '0'
            

        
        