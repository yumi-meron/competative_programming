class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        #extra space for counting sort
        lst = [0]* (max(costs)+1)
        #sorting by using the extra space
        for cost in costs:
            lst[cost] += 1

        icecreams = 0 #the amount of icecreams we can buy
        price = 0  #the price we are paying for those icecreams

        #iterating over my sorted counting sort list by keeping the price we paid and the icecreams we paid till now
        for i in range(len(lst)):
            if price + i*(lst[i]) <= coins:
                icecreams += lst[i]
                price += i*(lst[i])
            else:
                if lst[i] > 1:
                    for j in range(lst[i]):
                        if price + i <= coins:
                            price += i
                            icecreams += 1
                        else:
                            break
                    break
                    #once the price exceedes the coins we have , break

        return icecreams
    

        