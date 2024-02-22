class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        costs.sort(key = lambda x: abs(x[0] - x[1]), reverse = True)
        print(costs)
        n = len(costs) // 2
        acost,bcost = 0, 0
        maxcost = 0
        
        for a,b in costs:
            
            # if a == b:
            #     if acost < bcost:
            #         acost += 1
            #         maxcost += a
            #     else:
            #         bcost+=1
            #         maxcost += b
            # el
            if (a < b or  n - bcost == 0) and n-acost>0:
                acost+=1
                maxcost += a
                
            else:
                bcost+=1
                maxcost += b
            
        return maxcost

        