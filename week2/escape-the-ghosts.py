class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        #function to calculate the distance b/n the ghosts and the target
        def distance_from_target(lst,target):
            distance = sqrt(abs(lst[0]-target[0])+ abs(lst[1]-target[1]) )
            return distance
        
        #storing the distance b/n the ghosts and the target
        ghosts_distance = []
        for ghost in ghosts:
            ghosts_distance.append(distance_from_target(ghost,target))
        
        #calculating my distance from the target
        my_distance = distance_from_target([0,0],target)

        #checking if our distance is greater than ghost distance
        if min(ghosts_distance) <= my_distance:
            return False
        else:
            return True
        
        

        