class Solution:
    def numberOfMatches(self, n: int) -> int:
        matches = 0

        # until we are left with 1 team we will do the following operations
        while n>1:
            # if n is odd we will hold (n-1)/2 matches and (n-1)/2)+1 teams will be promoted to the next match
            if n %2 ==1:
                matches += ((n-1)/2)
                n = ((n-1)/2) + 1
            
            #if n is even we will have n/2 matches and n/2 teams will be promoted to the next match
            else:
                matches += n/2
                n /= 2

        return int(matches)
                

        