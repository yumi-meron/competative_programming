class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = list(zip(position,speed))
        combined.sort(key = lambda x: x[0], reverse = True)
        
        distance = []
        for pos, sp in combined:
            distance.append((target - pos) / sp)
        # print(distance)
        # fleet = 0
        stack = [distance[0]]
        for dis in distance[1:]:
            if stack and stack[-1] < dis:
                stack.append(dis)
            
        return len(stack)



