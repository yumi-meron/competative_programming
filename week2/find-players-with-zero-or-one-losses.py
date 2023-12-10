class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        losers = {}
        winners = {}
        players = set()

        for winner, loser in matches:
            players.add(winner)
            players.add(loser)
            losers[loser] = losers.get(loser, 0 ) + 1
            winners[winner] = winners.get(winner, 0 ) + 1

        only_winners = sorted(list(set(winners.keys()) - set(losers.keys())))
        only_one_lose = sorted([player for player in losers if losers.get(player,0) == 1])
        
        return [only_winners, only_one_lose]


        
     
        
        
        
        