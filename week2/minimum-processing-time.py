class Solution:
    def minProcessingTime(self, pTime: List[int], tasks: List[int]) -> int:
        pTime.sort()
        tasks.sort(reverse = True)
      
        temp = 0

        for i in range(len(tasks)):
            time = pTime[i//4] + tasks[i]
            temp = max(temp, time)
            
        return temp

        