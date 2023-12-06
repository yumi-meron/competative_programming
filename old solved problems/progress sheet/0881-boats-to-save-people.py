class Solution(object):
    def numRescueBoats(self, people, limit):
        """
        :type people: List[int]
        :type limit: int
        :rtype: int
        """
        boat = 0
        people.sort()
        i = 0
        j = len(people)-1
        while i<=j:
            if people[i] + people[j]>limit:
                boat += 1
                j -= 1
            elif people[i] + people[j] <= limit:
                boat +=1
                j -=1
                i +=1
        return boat
                