class OrderedStream:

    def __init__(self, n: int):
        self.lst = [0] *n
        self.ptr = 0     
        self.size = n
        

    def insert(self, idKey: int, value: str) -> List[str]:
        self.lst[idKey-1] = value
        ret = []
        while self.ptr < self.size and self.lst[self.ptr] != 0 :
            ret.append(self.lst[self.ptr])
            self.ptr += 1
        return ret
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)