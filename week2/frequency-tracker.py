class FrequencyTracker:

    def __init__(self):
        self.dic = {}   
        self.count = {}     

    def add(self, number: int) -> None:
        self.dic[number] = self.dic.get(number, 0) + 1
        self.count[self.dic[number]] = self.count.get(self.dic[number],0) + 1
        if self.dic[number]-1 in self.count:
            self.count[self.dic[number]-1] -= 1


        

    def deleteOne(self, number: int) -> None:
        if number in self.dic and self.dic[number] > 0:
            if self.dic[number] > 1:
                self.count[self.dic[number]-1] += 1

            self.count[self.dic[number]] -= 1
            self.dic[number] -= 1
        
        

    def hasFrequency(self, frequency: int) -> bool:
        return frequency in self.count and self.count[frequency]>0
            


        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)