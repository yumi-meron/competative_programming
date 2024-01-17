class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        pre = [0] * (n)
        for seats in bookings:
            start, end, seat = seats
            pre[start-1] += seat
            if end + 1 <= n: pre[end] -= seat
        for i in range(1,n):
            pre[i] += pre[i-1]
        return pre
