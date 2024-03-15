class TimeMap:

    def __init__(self):
       self.store = collections.defaultdict(list)
 

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key in self.store:
            idx = bisect.bisect(self.store[key], (timestamp, chr(127)))
            return self.store[key][idx-1][1] if idx else ""
        else:
            return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)