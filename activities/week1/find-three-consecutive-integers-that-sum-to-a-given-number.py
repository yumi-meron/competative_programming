class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        ans = []
        if num%3 == 0:
            x = num//3
            ans = [x-1,x,x+1]
        return ans
        