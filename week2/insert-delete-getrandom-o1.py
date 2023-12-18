class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.lst = []
        

    def insert(self, val: int) -> bool:
        if val not in self.dic:
            idx = len(self.lst)
            self.dic[val] = idx
            self.lst.append(val)
            return True
        return False



    def remove(self, val: int) -> bool:
        if val in self.dic:
            last_element, idx = self.lst[-1], self.dic[val]
            self.lst[idx], self.dic[last_element] = last_element, idx
            self.lst.pop()
            del self.dic[val]
            return True
        return False
        

    def getRandom(self) -> int:
        return random.choice(self.lst)
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()