class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        max_capacity = capacity
        steps = 0
        for i in range(len(plants)):
            if capacity < plants[i]:
                steps += (i*2)
                capacity = max_capacity
            
            steps+=1
            capacity -= plants[i]

        return steps



        