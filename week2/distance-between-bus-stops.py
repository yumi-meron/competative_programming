class Solution:
    def distanceBetweenBusStops(self, distance: List[int], start: int, destination: int) -> int:
        list_sum = sum(distance)
        starting = min(start,destination)
        end = max(start,destination)
        clockwise = sum(distance[starting:end])
        counter = list_sum - clockwise
        return min(clockwise,counter)




        