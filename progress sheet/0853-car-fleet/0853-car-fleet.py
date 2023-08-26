class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        times = [(target - pos) /sp for pos, sp in zip(position,speed) ]
        cars = sorted(zip(position, times), reverse = True)
        fleet = 0
        max_time = 0
        for _,t in cars:
            if t > max_time:
                fleet += 1
                max_time = t
        return fleet
            