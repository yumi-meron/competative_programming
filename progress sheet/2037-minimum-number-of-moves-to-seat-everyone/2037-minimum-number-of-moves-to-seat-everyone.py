class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        count = 0
        s = sorted(seats)
        st = sorted(students)
        for i in range(len(seats)):
            count += abs(s[i]-st[i])
        return count
        