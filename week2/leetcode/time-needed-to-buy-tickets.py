class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        sec = 0
        i = 0
        while tickets[k] != 0:
            if tickets[i%n] > 0:
                tickets[i%n] -= 1
                sec += 1
            if tickets[k] == 0:
                break
            i+=1
        return sec
        


        