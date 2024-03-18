class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.persons = persons
        count = defaultdict(int)

        self.winners = []
        winner = -1

        for i, person in enumerate(persons):
            count[person] += 1
            if count[person] >= count[winner]:
                winner = person
            self.winners.append(winner)

    def q(self, t: int) -> int:
        idx = bisect_right(self.times, t) - 1
        return self.winners[idx]
        


# Your TopVotedCandidate object will be instantiated and called as such:
# obj = TopVotedCandidate(persons, times)
# param_1 = obj.q(t)