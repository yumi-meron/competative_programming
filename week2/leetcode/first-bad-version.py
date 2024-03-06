# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        leftNum, rightNum = 1, n
        while leftNum <= rightNum:
            mid = (leftNum + rightNum) // 2
            if not isBadVersion(mid):
                leftNum = mid + 1
            elif isBadVersion(mid):
                rightNum = mid
            if leftNum == rightNum:
                return leftNum
            


        